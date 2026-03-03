import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json
import shutil

# CONFIGURATION
BASE_URL = "https://cobottooling.com"
DATA_FILE = 'data/data.csv'
TEMPLATES_DIR = 'templates'
OUTPUT_DIR = 'dist'
AUTHOR_NAME = "Dr. Aris Robotics"

# SETUP JINJA2 (Separates Logic from Design)
env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR, encoding='utf-8'),
    autoescape=select_autoescape(['html', 'xml'])
)

def build_site():
    print("🚀 Initializing high-authority build for cobotooling.com...")
    
    # 1. PREP OUTPUT
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(f"{OUTPUT_DIR}/solution", exist_ok=True)
    
    # 2. LOAD DATA
    df = pd.read_csv(DATA_FILE, encoding='utf-8-sig')
    
    # 3. GENERATE PRODUCT PAGES
    # This uses the product_layout.html you already have
    product_template = env.get_template('product_layout.html')
    for _, row in df.iterrows():
        # Create Structured Data for Google Rich Snippets
        schema = {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": row['Tool_Name'],
            "description": row['Pain_Point']
        }
        
        html = product_template.render(
            p=row, 
            schema=json.dumps(schema), 
            author=AUTHOR_NAME
        )
        
        with open(f"{OUTPUT_DIR}/solution/{row['Problem_ID']}.html", 'w', encoding='utf-8') as f:
            f.write(html)

    # 4. GENERATE CORNERSTONE PILLAR
    # This uses the guide-cobot-end-effectors.html logic
    pillar_template = env.get_template('pillar_layout.html')
    pillar_html = pillar_template.render(
        tools=df.to_dict(orient='records'),
        author=AUTHOR_NAME
    )
    with open(f"{OUTPUT_DIR}/index.html", 'w', encoding='utf-8') as f:
        f.write(pillar_html)

    # 5. SEO ASSETS
    # Sitemap ensures Google indexes ALL your programmatic pages
    with open(f"{OUTPUT_DIR}/sitemap.xml", 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for pid in df['Problem_ID']:
            f.write(f'  <url><loc>{BASE_URL}/solution/{pid}.html</loc></url>\n')
        f.write('</urlset>')

    print("✅ Build Complete. Files are in /dist")

if __name__ == "__main__":
    build_site()