from database.connection import db

disease_info_collection = db['disease_info']

disease_data = [
    {
    "_id": "Apple___Apple_scab",
    "title": "Apple Scab",
    "description": "Apple Scab is caused by the fungus *Venturia inaequalis*. It produces dark, scabby lesions on leaves, fruit, and stems, leading to defoliation and reduced fruit quality. The disease thrives in cool, wet conditions and can be managed through the use of resistant varieties, proper sanitation, and fungicide applications.For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/apple-scab",
        "https://extension.umn.edu/disease-management/apple-scab",
        "https://www.thespruce.com/managing-apple-scab-1402587"
    ]
},
    {
    "_id": "Apple___Black_rot",
    "title": "Black Rot",
    "description": "Black Rot of apple is caused by the fungus *Botryosphaeria obtusa*. It produces dark, sunken lesions on fruit, leaves, and stems, leading to fruit rot and defoliation. The disease thrives in warm, humid conditions and can be managed through the use of resistant varieties, proper sanitation, and fungicide applications. For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/black-rot-of-apple",
        "https://extension.umn.edu/disease-management/black-rot",
        "https://www.thespruce.com/managing-black-rot-in-apples-1402587"
    ]
},
    {
    "_id": "Apple___Cedar_apple_rust",
    "title": "Cedar Apple Rust",
    "description": "Cedar Apple Rust is caused by the fungus *Gymnosporangium juniperi-virginianae*. It produces bright orange lesions on leaves and fruit, leading to defoliation and reduced fruit quality. The disease requires both apple and cedar trees to complete its life cycle and can be managed through the use of resistant varieties, proper sanitation, and fungicide applications. For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/cedar-apple-rust",
        "https://extension.umn.edu/disease-management/cedar-apple-rust",
        "https://www.thespruce.com/managing-cedar-apple-rust-1402587"
    ]
},
    {
    "_id": "Apple___healthy",
    "title": "Powdery Mildew",
    "description": "Healthy apple trees are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper pruning, adequate irrigation, and balanced fertilization. Healthy apple trees produce high-quality fruit and have a longer productive lifespan. For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/powdery-mildew-of-cherry",
        "https://extension.umn.edu/disease-management/powdery-mildew",
        "https://www.thespruce.com/managing-powdery-mildew-in-cherries-1402587"
    ]
},
    {
    "_id": "Cherry_(including_sour)___healthy",
    "title": "Gray Leaf Spot",
    "description": "Powdery Mildew of cherry is caused by the fungus *Podosphaera clandestina*. It produces white, powdery spots on leaves and stems, leading to reduced photosynthesis and yield. The disease thrives in warm, dry conditions and can be managed through the use of resistant varieties, proper spacing, and fungicide applications.For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/gray-leaf-spot-of-corn",
        "https://extension.umn.edu/disease-management/gray-leaf-spot",
        "https://www.thespruce.com/managing-gray-leaf-spot-in-corn-1402587"
    ]
},
    {
    "_id": "Corn_(maize)___Common_rust_",
    "title": "Common Rust",
    "description": "Common Rust of corn is caused by the fungus *Puccinia sorghi*. It produces small, reddish-brown pustules on leaves, leading to reduced photosynthesis and yield. The disease thrives in cool, wet conditions and can be managed through the use of resistant varieties, proper sanitation, and fungicide applications.For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/common-rust-of-corn",
        "https://extension.umn.edu/disease-management/common-rust",
        "https://www.thespruce.com/managing-common-rust-in-corn-1402587"
    ]
},
    {
    "_id": "Corn_(maize)___Northern_Leaf_Blight",
    "title": "Northern Leaf Blight",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/northern-leaf-blight-of-corn",
        "https://extension.umn.edu/disease-management/northern-leaf-blight",
        "https://www.thespruce.com/managing-northern-leaf-blight-in-corn-1402587"
    ]
},
    {
    "_id": "Corn_(maize)___healthy\nHealthy corn plants are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper fertilization, and timely irrigation. Healthy corn plants produce high-quality grain and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Corn - The Old Farmer's Almanac](https://www.almanac.com/plant/corn)\n- [Corn Growing Guide - The Spruce](https://www.thespruce.com/corn-growing-guide-1402587)\n- [Corn Cultivation: Tips for a Healthy Crop - The Farming Insider](https://thefarminginsider.com/corn-cultivation/)\n\n### 12. Grape___Black_rot",
    "title": "Black Rot",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/black-rot-of-grape",
        "https://extension.umn.edu/disease-management/black-rot",
        "https://www.thespruce.com/managing-black-rot-in-grapes-1402587"
    ]
},
    {
    "_id": "Grape___Esca_(Black_Measles)",
    "title": "Esca",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/esca-black-measles-of-grape",
        "https://extension.umn.edu/disease-management/esca",
        "https://www.thespruce.com/managing-esca-in-grapes-1402587"
    ]
},
    {
    "_id": "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "title": "Leaf Blight",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/leaf-blight-of-grape",
        "https://extension.umn.edu/disease-management/leaf-blight",
        "https://www.thespruce.com/managing-leaf-blight-in-grapes-1402587"
    ]
},
    {
    "_id": "Grape___healthy\nHealthy grapevines are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper pruning, adequate irrigation, and balanced fertilization. Healthy grapevines produce high-quality fruit and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Grapes - The Old Farmer's Almanac](https://www.almanac.com/plant/grapes)\n- [Grape Growing Guide - The Spruce](https://www.thespruce.com/grape-growing-guide-1402587)\n- [Grape Cultivation: Tips for a Healthy Crop - The Farming Insider](https://thefarminginsider.com/grape-cultivation/)\n\n### 16. Orange___Haunglongbing_(Citrus_greening)",
    "title": "Huanglongbing (HLB)",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/huanglongbing-citrus-greening",
        "https://extension.umn.edu/disease-management/citrus-greening",
        "https://www.thespruce.com/managing-citrus-greening-1402587"
    ]
},
    {
    "_id": "Peach___Bacterial_spot",
    "title": "Bacterial Spot",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/bacterial-spot-of-peach",
        "https://extension.umn.edu/disease-management/bacterial-spot",
        "https://www.thespruce.com/managing-bacterial-spot-in-peaches-1402587"
    ]
},
    {
    "_id": "Peach___healthy\nHealthy peach trees are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper pruning, adequate irrigation, and balanced fertilization. Healthy peach trees produce high-quality fruit and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Peach Trees - The Old Farmer's Almanac](https://www.almanac.com/plant/peach-trees)\n- [Peach Tree Growing Guide - The Spruce](https://www.thespruce.com/peach-tree-growing-guide-1402587)\n- [Peach Tree Cultivation: Tips for a Healthy Crop - The Farming Insider](https://thefarminginsider.com/peach-tree-cultivation/)\n\n### 19. Pepper,_bell___Bacterial_spot",
    "title": "Bacterial Spot",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/bacterial-spot-of-bell-pepper",
        "https://extension.umn.edu/disease-management/bacterial-spot",
        "https://www.thespruce.com/managing-bacterial-spot-in-bell-peppers-1402587"
    ]
},
    {
    "_id": "Pepper,_bell___healthy\nHealthy bell pepper plants are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper pruning, adequate irrigation, and balanced fertilization. Healthy bell pepper plants produce high-quality fruit and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Bell Peppers - The Old Farmer's Almanac](https://www.almanac.com/plant/bell-peppers)\n- [Bell Pepper Growing Guide - The Spruce](https://www.thespruce.com/bell-pepper-growing-guide-1402587)\n- [Bell Pepper Cultivation: Tips for a Healthy Crop - The Farming Insider](https://thefarminginsider.com/bell-pepper-cultivation/)\n\n### 21. Potato___Early_blight",
    "title": "Early Blight",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/early-blight-of-potato",
        "https://extension.umn.edu/disease-management/early-blight",
        "https://www.thespruce.com/managing-early-blight-in-potatoes-1402587"
    ]
},
    {
    "_id": "Potato___Late_blight",
    "title": "Late Blight",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/late-blight-of-potato",
        "https://extension.umn.edu/disease-management/late-blight",
        "https://www.thespruce.com/managing-late-blight-in-potatoes-1402587"
    ]
},
    {
    "_id": "Potato___healthy\nHealthy potato plants are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper hilling, adequate irrigation, and balanced fertilization. Healthy potato plants produce high-quality tubers and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Potatoes - The Old Farmer's Almanac](https://www.almanac.com/plant/potatoes)\n- [Potato Growing Guide - The Spruce](https://www.thespruce.com/potato-growing-guide-1402587)\n- [Potato Cultivation: Tips for a Healthy Crop - The Farming Insider](https://thefarminginsider.com/potato-cultivation/)\n\n### 24. Raspberry___healthy\nHealthy raspberry plants are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper pruning, adequate irrigation, and balanced fertilization. Healthy raspberry plants produce high-quality fruit and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Raspberries - The Old Farmer's Almanac](https://www.almanac.com/plant/raspberries)\n- [Raspberry Growing Guide - The Spruce](https://www.thespruce.com/raspberry-growing-guide-1402587)\n- [Raspberry Cultivation: Tips for a Healthy Crop - The Farming Insider](https://thefarminginsider.com/raspberry-cultivation/)\n\n### 25. Soybean___healthy\nHealthy soybean plants are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper crop rotation, adequate irrigation, and balanced fertilization. Healthy soybean plants produce high-quality beans and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Soybeans - The Old Farmer's Almanac](https://www.almanac.com/plant/soybeans)\n- [Soybean Growing Guide - The Spruce](https://www.thespruce.com/soybean-growing-guide-1402587)\n- [Soybean Cultivation: Tips for a Healthy Crop - The Farming Insider](https://thefarminginsider.com/soybean-cultivation/)\n\n### 26. Squash___Powdery_mildew",
    "title": "Powdery Mildew",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://www.gardeningknowhow.com/edible/vegetables/squash/powdery-mildew-in-squash.htm",
        "https://savvygardening.com/powdery-mildew-on-squash/",
        "https://www.evergreenseeds.com/how-to-treat-powdery-mildew-on-squash/"
    ]
},
    {
    "_id": "Strawberry___Leaf_scorch",
    "title": "Leaf Scorch",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/leaf-scorch-of-strawberry",
        "https://www.epicgardening.com/strawberry-diseases/",
        "https://ipm.ucanr.edu/pmg/garden/fruit/DISEASE/leafscorch.html"
    ]
},
    {
    "_id": "Strawberry___healthy\nHealthy strawberry plants are those that are free from diseases and pests, and are well-maintained through proper cultural practices. Key practices include selecting disease-resistant varieties, proper pruning, adequate irrigation, and balanced fertilization. Healthy strawberry plants produce high-quality fruit and have a longer productive lifespan.\n\nFor more details, you can refer to:\n- [How to Grow Strawberries: The Ultimate Guide | Rivulis](https://www.rivulis.com/how-to-grow-strawberries/)\n- [How to Grow Strawberries - Tractor Supply Co.](https://www.tractorsupply.com/tsc/cms/life-out-here/garden/growing-guides/fruits/how-to-grow-strawberries)\n- [How to Plant & Grow The Perfect Strawberries - The Botanic Home](https://thebotanichome.com/how-to-grow-strawberries/)\n\n### 29. Tomato___Bacterial_spot",
    "title": "Bacterial Spot",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://hort.extension.wisc.edu/articles/bacterial-spot-of-tomato/",
        "https://extension.umn.edu/disease-management/bacterial-spot-tomato-and-pepper",
        "https://content.ces.ncsu.edu/bacterial-spot-of-pepper-and-tomato"
    ]
},
    {
    "_id": "Tomato___Early_blight",
    "title": "Early Blight",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/early-blight-of-tomato",
        "https://extension.umn.edu/disease-management/early-blight-tomato-and-potato",
        "https://www.almanac.com/pest/early-blight"
    ]
},
    {
    "_id": "Tomato___Late_blight",
    "title": "Late Blight",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/tomato-late-blight",
        "https://www.epicgardening.com/late-blight-tomatoes/",
        "https://www.thespruce.com/identify-treat-prevent-tomato-diseases-7153094"
    ]
},
    {
    "_id": "Tomato___Leaf_Mold",
    "title": "Leaf Mold",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://extension.umn.edu/disease-management/tomato-leaf-mold",
        "https://www.vegetables.cornell.edu/pest-management/disease-factsheets/tomato-leaf-mold/",
        "https://www.gardeningknowhow.com/edible/vegetables/tomato/managing-tomato-leaf-mold.htm"
    ]
},
    {
    "_id": "Tomato___Septoria_leaf_spot",
    "title": "Septoria Leaf Spot",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/septoria-leaf-spot-of-tomato",
        "https://extension.illinois.edu/plant-problems/septoria-leaf-spot-tomato",
        "https://gardenerspath.com/how-to/disease-and-pests/septoria-leaf-spot-tomatoes/"
    ]
},
    {
    "_id": "Tomato___Spider_mites Two-spotted_spider_mite",
    "title": "Two-Spotted Spider Mite",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://entomology.ca.uky.edu/ef310",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7952643/",
        "https://ag.umass.edu/vegetable/fact-sheets/two-spotted-spider-mite"
    ]
},
    {
    "_id": "Tomato___Target_Spot",
    "title": "Target Spot",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://www.vegetables.bayer.com/ca/en-ca/resources/agronomic-spotlights/target-spot-of-tomato.html",
        "https://www.gardeningknowhow.com/edible/vegetables/tomato/target-spot-on-tomatoes.htm",
        "https://vegcropshotline.org/article/new-disease-report-target-spot-of-tomato/"
    ]
},
    {
    "_id": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "title": "Tomato Yellow Leaf Curl Virus (TYLCV)",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://content.ces.ncsu.edu/tomato-yellow-leaf-curl-virus",
        "https://en.wikipedia.org/wiki/Tomato_yellow_leaf_curl_virus",
        "https://link.springer.com/book/10.1007/978-1-4020-4769-5"
    ]
},
    {
    "_id": "Tomato___Tomato_mosaic_virus",
    "title": "Tomato Mosaic Virus (ToMV)",
    "description": "For more details, you can refer to:",
    "symptoms": "Check for spots, lesions, or discoloration on leaves, stems, or fruits.",
    "treatment": "Use resistant varieties, maintain hygiene, and apply fungicides as necessary.",
    "sources": [
        "https://u.osu.edu/vegetablediseasefacts/tomato-diseases/high-tunnel-diseases/tomato-mosaic/",
        "https://en.wikipedia.org/wiki/Tomato_mosaic_virus",
        "https://extension.umn.edu/disease-management/tomato-viruses"
    ]
},
]

disease_info_collection.delete_many({})
disease_info_collection.insert_many(disease_data)
print('🦠 All plant disease info inserted successfully!')
