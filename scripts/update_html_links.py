import re

def main():
    html_file = "reports/top10_potential_products_analysis.html"
    
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    replacements = {
        "ai_mockups/mockup_1.jpg": "https://wanderprints.com/cdn/shop/files/MKDEF_61570a26-6b2e-4c22-a95f-f7ed5032b491.webp?v=1775814500&width=1000",
        "ai_mockups/mockup_2.jpg": "https://wanderprints.com/cdn/shop/files/Custom_Photo_Faceless_Portrait_Best_Dad_Mom_Ever_-_Personalized_Acrylic_Car_Vent_Clip.webp?v=1775817294&width=1000",
        "ai_mockups/mockup_3.jpg": "https://wanderprints.com/cdn/shop/files/Mom_Grandma_We_Love_You_-_Personalized_Flower_In_Glass_Angel_Figurine.webp?v=1775816685&width=1000",
        "ai_mockups/mockup_4.jpg": "https://wanderprints.com/cdn/shop/files/America250thAnniversaryFamilyName-PersonalizedHorizontalBanner-DH378-CLA2799-MKDEF.webp?v=1775806320&width=1000",
        "ai_mockups/mockup_5.jpg": "https://wanderprints.com/cdn/shop/files/TU350-DSR838-MKDef.webp?v=1775815337&width=1000",
        "ai_mockups/mockup_6.jpg": "https://wanderprints.com/cdn/shop/files/DEF_8f92f977-9855-44e8-afb1-fac10901cf40.webp?v=1775814009&width=1000",
        "ai_mockups/mockup_7.jpg": "https://wanderprints.com/cdn/shop/files/PT1998-CIN4428-MKDEF.webp?v=1775874494&width=1000",
        "ai_mockups/mockup_8.jpg": "https://wanderprints.com/cdn/shop/files/CustomPhotoOutlineSketchBestiesSistersForever-MKDEF.webp?v=1775727827&width=1000",
        "ai_mockups/mockup_9.jpg": "https://wanderprints.com/cdn/shop/files/GraduationKidDinosaurUnicorn-PersonalizedKidGraduationStole-HA244-CLA2741-MKDEF.webp?v=1775814000&width=1000",
        "ai_mockups/mockup_10.jpg": "https://wanderprints.com/cdn/shop/files/CheersToTheNewGraduate-PersonalizedBeerGlass-TH271-VKT657-DEF.webp?v=1775795175&width=1000"
    }

    for old_img, new_img in replacements.items():
        content = content.replace(old_img, new_img)
        
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()