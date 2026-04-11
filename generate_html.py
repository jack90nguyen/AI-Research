import json

products_data = [
    {
        "rank": 1,
        "title": "Grandma's Garden Family Birth Flower Bouquet - Personalized Acrylic Plaque",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Grandma_s_Garden_Family_Birth_Flower_Bouquet_Flowers_Gifts_For_Mom_Grandma_Personalized_Acrylic_Plaque_1.jpg?v=1775733691",
        "link": "https://macorner.co/products/grandmas-garden-family-birth-flower-bouquet-flowers-gifts-for-mom-grandma-personalized-acrylic-plaque-ma8fpamx9",
        "audience": "Phụ nữ (35-65 tuổi), những người đã có gia đình. Mua làm quà tặng cho mẹ đẻ, mẹ chồng hoặc bà nhân dịp Mother's Day, Sinh nhật, hoặc Lễ tạ ơn.",
        "insight": "Concept \"Vườn của Bà\" (Grandma's Garden) nơi mỗi nụ hoa đại diện cho một người cháu đánh mạnh vào lòng tự hào gia đình. Chất liệu Acrylic trong suốt mang lại cảm giác hiện đại, sang trọng hơn in canvas/poster thông thường, cho phép bán giá cao nhưng phí ship rẻ.",
        "scale": "<li><strong>Scale Đối tượng:</strong> Đổi title thành \"Mom's Garden\", \"Auntie's Garden\", \"Nana's Garden\".</li><li><strong>Scale Thiết kế:</strong> Thay thế hoa tháng sinh bằng hình chibi các cháu, hoặc dấu vân tay, hoặc thú cưng (Cat Mom/Dog Mom).</li><li><strong>Scale Sản phẩm:</strong> Áp dụng cùng thiết kế này lên Chăn (Fleece Blanket), Gối vuông (Throw Pillow).</li>",
        "scale_images": [
            "https://placehold.co/300x300/e2f0cb/2c3e50?text=Mom's+Garden%5Cn(Acrylic+Plaque)",
            "https://placehold.co/300x300/e2f0cb/2c3e50?text=Cat+Mom's+Garden%5Cn(Paw+Prints)",
            "https://placehold.co/300x300/e2f0cb/2c3e50?text=Garden+Theme%5Cn(Throw+Pillow)"
        ],
        "scale_labels": ["Đổi tệp sang Mẹ", "Đổi tệp sang Thú cưng", "Mở rộng sang Gối Sofa"]
    },
    {
        "rank": 2,
        "title": "Mother & Children Forever Linked Together - Personalized Flower In Glass Angel Figurines",
        "price": "$39.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Mother_Children_Forever_Linked_Together_Personalized_Flower_In_Glass_Angel_Figurines_1.jpg?v=1775793170",
        "link": "https://macorner.co/products/mother-children-forever-linked-together-personalized-flower-in-glass-angel-figurines-marjtp671",
        "audience": "Con cái đã trưởng thành mua tặng mẹ, hoặc chồng mua tặng vợ nhân dịp kỷ niệm sinh con. Phù hợp tệp khách hàng thích decor nhà cửa phong cách cổ điển, tâm linh.",
        "insight": "Sản phẩm ngách vật lý cực độc đáo. Khác với Print-on-demand truyền thống (áo, cốc), tượng thiên thần thủy tinh có giá trị cảm nhận (Perceived Value) rất cao. Người nhận sẽ đặt nó ở phòng khách/tủ kính. Mức giá $39.95 mang lại biên lợi nhuận tuyệt vời.",
        "scale": "<li><strong>Scale Dịp lễ:</strong> Thay đổi thông điệp để bán vào dịp Tưởng niệm (In Loving Memory), Giáng sinh (Christmas Ornament).</li><li><strong>Scale Quà tặng:</strong> Bán kèm hộp quà cao cấp hoặc đèn LED chiếu đế.</li>",
        "scale_images": [
            "https://placehold.co/300x300/fce4ec/2c3e50?text=In+Loving+Memory%5Cn(Memorial+Gift)",
            "https://placehold.co/300x300/fce4ec/2c3e50?text=Christmas+Angel%5Cn(Tree+Ornament)",
            "https://placehold.co/300x300/fce4ec/2c3e50?text=Premium+Gift+Box%5Cn(+LED+Base)"
        ],
        "scale_labels": ["Quà tưởng niệm (Memorial)", "Đồ trang trí Giáng sinh", "Bán kèm Đế LED/Hộp quà"]
    },
    {
        "rank": 3,
        "title": "Mother & Daughters Forever Linked Together - Personalized Bracelet",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Mother_Daughters_Forever_Linked_Together_Personalized_Bracelet_1.jpg?v=1775812885",
        "link": "https://macorner.co/products/mother-daughters-forever-linked-together-personalized-bracelet-makcmi5m8",
        "audience": "Phụ nữ trẻ (18-40 tuổi), Gen Z, Millennials mua tặng mẹ hoặc ngược lại. Những người thích trang sức tinh tế, dễ đeo hàng ngày.",
        "insight": "Trang sức cá nhân hóa khắc tên/charm là top seller vì tính thực dụng cao. Một chiếc vòng tay nhỏ nhắn kết nối mẹ con tinh tế hơn nhiều so với áo thun. Phí ship quốc tế cho đồ trang sức là cực rẻ.",
        "scale": "<li><strong>Scale Đối tượng:</strong> Mở rộng sang ngách Bạn thân (Besties), Cặp đôi (Couples khắc tọa độ).</li><li><strong>Scale Volume:</strong> Chiến lược BUNDLE bán set 2, 3, 4 vòng với giá chiết khấu.</li>",
        "scale_images": [
            "https://placehold.co/300x300/fff3e0/2c3e50?text=Soul+Sisters%5Cn(Friendship)",
            "https://placehold.co/300x300/fff3e0/2c3e50?text=Custom+Coordinates%5Cn(Couples)",
            "https://placehold.co/300x300/fff3e0/2c3e50?text=Family+Bundle%5Cn(Set+of+3)"
        ],
        "scale_labels": ["Vòng tay tình bạn", "Vòng tay cặp đôi (Tọa độ)", "Bán Combo (Bundle 3 vòng)"]
    },
    {
        "rank": 4,
        "title": "Custom Birth Flower & Name Gift For Book Lovers - Personalized Wooden Plaque",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Custom_Birth_Flower_Name_Gift_For_Book_Lovers_Friend_Personalized_Book_Nook_1.jpg?v=1775818891",
        "link": "https://macorner.co/products/custom-birth-flower-name-gift-for-book-lovers-friend-personalized-wooden-plaque-mauexidkv",
        "audience": "Hội đam mê đọc sách (Bookworms), giáo viên, thủ thư, học sinh/sinh viên. Độ tuổi từ 15-50 tuổi, có sở thích sưu tầm sách.",
        "insight": "Sự kết hợp chéo (Cross-niche) hoàn hảo giữa ngách \"Book Lover\" và trend \"Birth Flower\". Sản phẩm bảng gỗ dạng Book Nook vừa dùng để trang trí kệ sách, vừa có thể làm đồ chặn sách. Thiết kế rustic mộc mạc.",
        "scale": "<li><strong>Scale Thiết kế:</strong> Thay hình cô gái bằng kệ sách có in tên các cuốn sách yêu thích.</li><li><strong>Scale Ngách:</strong> Mở rộng cho ngách Game Thủ, Mọt Phim điện ảnh (Movie Lovers).</li><li><strong>Cross-sell:</strong> Bán kèm Bookmark gỗ.</li>",
        "scale_images": [
            "https://placehold.co/300x300/e8f5e9/2c3e50?text=Custom+Bookshelf%5Cn(Favorite+Books)",
            "https://placehold.co/300x300/e8f5e9/2c3e50?text=Gamer's+Corner%5Cn(Setup+Decor)",
            "https://placehold.co/300x300/e8f5e9/2c3e50?text=Matching+Wooden%5CnBookmark"
        ],
        "scale_labels": ["Thiết kế kệ sách yêu thích", "Đổi ngách sang Game Thủ", "Bán chéo Bookmark Gỗ"]
    },
    {
        "rank": 5,
        "title": "Toile De Jouy Custom Vintage Photo Mom And Children - Personalized Wine Tumbler",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Toile_De_Jouy_Custom_Vintage_Photo_Mom_And_Children_Thank_You_Gifts_For_Mom_Personalized_Wine_Tumbler_1.jpg?v=1775787501",
        "link": "https://macorner.co/products/toile-de-jouy-custom-vintage-photo-mom-and-children-thank-you-gifts-for-mom-personalized-wine-tumbler-mae9u7vzx",
        "audience": "Phụ nữ 25-55 tuổi, thích phong cách quý tộc, cổ điển, nghệ thuật. Những người có thói quen uống trà, cà phê, hoặc rượu vang.",
        "insight": "\"Toile De Jouy\" là họa tiết đồng quê Pháp đang trending. Việc mix pattern này với ảnh gia đình dạng vintage filter tạo sự khác biệt lớn. Ly giữ nhiệt (Tumbler) là sản phẩm dùng hàng ngày thực tế.",
        "scale": "<li><strong>Scale Sản phẩm:</strong> In pattern \"Toile De Jouy\" lên Túi Tote, Vỏ điện thoại, Chăn (Blanket).</li><li><strong>Scale Kỹ thuật:</strong> Thêm filter chuyển ảnh thật thành tranh màu nước (Watercolor).</li>",
        "scale_images": [
            "https://placehold.co/300x300/e3f2fd/2c3e50?text=Toile+De+Jouy%5Cn(Tote+Bag)",
            "https://placehold.co/300x300/e3f2fd/2c3e50?text=Watercolor+Filter%5Cn(Artistic+Photo)",
            "https://placehold.co/300x300/e3f2fd/2c3e50?text=Toile+De+Jouy%5Cn(Fleece+Blanket)"
        ],
        "scale_labels": ["Mở rộng sang Túi Tote", "Filter Ảnh Màu Nước", "Mở rộng sang Chăn (Blanket)"]
    },
    {
        "rank": 6,
        "title": "Custom Football Mom, Grandma - Personalized Shirt",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Custom_Football_Mom_Grandma_Personalized_Shirt_1.jpg?v=1775812760",
        "link": "https://macorner.co/products/custom-football-mom-grandma-personalized-shirt-ma7oh4sxt",
        "audience": "Phụ huynh ở Mỹ (Mẹ và Bà) có con/cháu tham gia các đội thể thao trường học hoặc câu lạc bộ.",
        "insight": "Văn hóa tự hào thể thao học đường ở Mỹ rất lớn. Các bà mẹ (Sports Moms) coi việc mặc áo in tên/số áo của con như niềm kiêu hãnh. Áo thun là sản phẩm dễ mua, form unisex.",
        "scale": "<li><strong>Scale Môn thể thao:</strong> Nhân bản sang Baseball Mom, Soccer Mom, Hockey Mom.</li><li><strong>Scale Theo Mùa:</strong> Chuyển sang áo Hoodie, Sweatshirt cho mùa đông.</li><li><strong>Scale Phụ trợ:</strong> Bán kèm bình giữ nhiệt dung tích lớn (Sport Jugs).</li>",
        "scale_images": [
            "https://placehold.co/300x300/fff8e1/2c3e50?text=Baseball+Mom%5Cn(New+Sport)",
            "https://placehold.co/300x300/fff8e1/2c3e50?text=Winter+Season%5Cn(Hoodie/Sweatshirt)",
            "https://placehold.co/300x300/fff8e1/2c3e50?text=Sports+Mom%5Cn(Large+Jug/Tumbler)"
        ],
        "scale_labels": ["Đổi môn (Baseball/Soccer)", "Bán Hoodie mùa đông", "Bình giữ nhiệt thể thao"]
    },
    {
        "rank": 7,
        "title": "Grandma's Garden Love Grows Here - Personalized Ceramic Plant Pot",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Grandmas-Garden-Love-Grows-Here-Gift-For-Grandma-Personalized-Ceramic-Plant-Pot_1.jpg?v=1775814571",
        "link": "https://macorner.co/products/grandmas-garden-love-grows-here-gift-for-grandma-personalized-ceramic-plant-pot-mae84c5wb",
        "audience": "Những người lớn tuổi (Bà, Mẹ) có sở thích làm vườn (Gardening), yêu cây cối (Plant lovers).",
        "insight": "Chậu cây gốm sứ là sản phẩm thực tế. Nhìn thấy tên các cháu trên chậu cây mỗi ngày khi tưới nước tạo ra giá trị tinh thần bền vững hơn rất nhiều so với quần áo.",
        "scale": "<li><strong>Scale Nhóm Pet:</strong> Đổi thành \"Cat Mom's Garden\" hoặc \"Crazy Plant Lady\".</li><li><strong>Scale Bundle:</strong> Bán theo set 3 chậu nhỏ (cho cây sen đá).</li><li><strong>Sản phẩm đi kèm:</strong> Bộ dụng cụ làm vườn mini khắc tên.</li>",
        "scale_images": [
            "https://placehold.co/300x300/f1f8e9/2c3e50?text=Crazy+Plant+Lady%5Cn(Cat+Pot)",
            "https://placehold.co/300x300/f1f8e9/2c3e50?text=Bundle+Set%5Cn(3+Mini+Pots)",
            "https://placehold.co/300x300/f1f8e9/2c3e50?text=Engraved+Wood%5Cn(Garden+Tools)"
        ],
        "scale_labels": ["Niche Mèo & Cây cối", "Combo 3 Chậu Sen Đá", "Dụng cụ làm vườn khắc tên"]
    },
    {
        "rank": 8,
        "title": "A Sweet Ending To A New Beginning Graduation - Personalized Wooden Plaque",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/A_Sweet_Ending_To_A_New_Beginning_Graduation_Personalized_Book_Nook_1.jpg?v=1775806682",
        "link": "https://macorner.co/products/a-sweet-ending-to-a-new-beginning-graduation-personalized-wooden-plaque-maknxv5fl",
        "audience": "Phụ huynh, bạn bè, người thân của học sinh/sinh viên chuẩn bị tốt nghiệp.",
        "insight": "Mùa tốt nghiệp (tháng 5, 6) là mỏ vàng POD. Quà tốt nghiệp mang tính lưu niệm cao. Bảng gỗ khắc tên, trường, năm tốt nghiệp có giá trị trưng bày lâu dài trên bàn làm việc.",
        "scale": "<li><strong>Scale Ngành Nghề:</strong> Thiết kế riêng cho Tốt nghiệp Y tá (Nurse), Bác sĩ, Luật sư.</li><li><strong>Scale Sản phẩm:</strong> Chuyển thiết kế lên Ly cà phê giữ nhiệt hoặc Khung ảnh tốt nghiệp.</li>",
        "scale_images": [
            "https://placehold.co/300x300/e8eaf6/2c3e50?text=Nurse+Graduation%5Cn(Niche+Down)",
            "https://placehold.co/300x300/e8eaf6/2c3e50?text=Graduation+Tears%5Cn(Coffee+Tumbler)",
            "https://placehold.co/300x300/e8eaf6/2c3e50?text=Graduation%5Cn(Custom+Photo+Frame)"
        ],
        "scale_labels": ["Tốt nghiệp Ngành Y/Nurse", "Ly Cà Phê Tốt Nghiệp", "Khung Ảnh Tốt Nghiệp"]
    },
    {
        "rank": 9,
        "title": "To Mom From The Reasons You Drink - Personalized Leather Wine Bag",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/To_Mom_From_The_Reasons_You_Drink_Fun_Gifts_For_Mom_Wife_Personalized_Leather_Wine_Bag_1.jpg?v=1775721149",
        "link": "https://macorner.co/products/to-mom-from-the-reasons-you-drink-fun-gifts-for-mom-wife-personalized-leather-wine-bag-mak8u87ye",
        "audience": "Người con trưởng thành, hoặc chồng mua tặng vợ. Tệp khách hài hước, thích uống rượu vang.",
        "insight": "Ngách Hài hước (Humor). Một món quà \"cà khịa\" dí dỏm thu hút sự chú ý cực mạnh trên quảng cáo. Túi da thật sự tạo sự sang trọng bù đắp cho câu quote vui nhộn.",
        "scale": "<li><strong>Scale Thông điệp:</strong> Áp dụng lên Ông Bố (Lý do bố uống bia), Giáo viên.</li><li><strong>Scale Sản phẩm:</strong> Áp dụng lên Ly rượu vang (Stemless), Đế lót ly bằng đá.</li>",
        "scale_images": [
            "https://placehold.co/300x300/fce4ec/2c3e50?text=Reasons+Dad+Drinks%5Cn(Whiskey+Glass)",
            "https://placehold.co/300x300/fce4ec/2c3e50?text=Teacher's+Wine%5Cn(Humorous+Bag)",
            "https://placehold.co/300x300/fce4ec/2c3e50?text=Humorous+Quote%5Cn(Stone+Coasters)"
        ],
        "scale_labels": ["Đổi sang Tệp Bố (Uống Bia/Whiskey)", "Đổi sang Tệp Giáo viên", "Đế lót ly đá (Coasters)"]
    },
    {
        "rank": 10,
        "title": "Girls Trip Summer - Personalized Wine Tumbler",
        "price": "$29.95",
        "image": "https://cdn.shopify.com/s/files/1/0626/0421/4428/files/Girls_Trip_Summer_Personalized_Wine_Tumbler_1.jpg?v=1775717955",
        "link": "https://macorner.co/products/girls-trip-summer-personalized-wine-tumbler-max6p0a3k",
        "audience": "Nhóm bạn nữ, hội chị em đi du lịch hè, hoặc tiệc độc thân (Bachelorette party).",
        "insight": "Sức mạnh của ngách Du lịch nhóm là tính Lan truyền. Khách hàng thường mua số lượng lớn cho cả nhóm (3-10 cái). Ly Tumbler giữ nhiệt lạnh rất tốt cho bãi biển.",
        "scale": "<li><strong>Scale Chủ đề:</strong> Mở rộng \"Vegas Trip\", \"Winter Ski Trip\", \"Cruise Squad\".</li><li><strong>Scale Bulk Order:</strong> Chiết khấu số lượng lớn.</li><li><strong>Bundle:</strong> Tumbler + Áo thun nhóm + Túi Tote.</li>",
        "scale_images": [
            "https://placehold.co/300x300/e0f7fa/2c3e50?text=Winter+Ski+Trip%5Cn(Custom+Tumbler)",
            "https://placehold.co/300x300/e0f7fa/2c3e50?text=Cruise+Squad%5Cn(Group+Tumblers)",
            "https://placehold.co/300x300/e0f7fa/2c3e50?text=Girls+Trip+Bundle%5Cn(Tumbler+%2B+Tote)"
        ],
        "scale_labels": ["Du lịch mùa đông (Trượt tuyết)", "Du lịch Tàu biển (Cruise)", "Bán Combo (Ly + Túi Tote)"]
    }
]

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top 10 Sản Phẩm Tiềm Năng - Macorner (Kèm Hình Ảnh Scale)</title>
    <style>
        :root {
            --primary: #2c3e50;
            --secondary: #3498db;
            --accent: #e74c3c;
            --bg: #f8f9fa;
            --card-bg: #ffffff;
            --text: #333333;
            --border: #e0e0e0;
        }
        body {
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background-color: var(--bg);
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: auto;
        }
        .header {
            text-align: center;
            margin-bottom: 50px;
            padding: 40px 20px;
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        h1 {
            color: var(--primary);
            margin: 0 0 10px 0;
            font-size: 2.2rem;
        }
        .subtitle {
            color: #666;
            font-size: 1.1rem;
        }
        .product-card {
            display: flex;
            flex-direction: column;
            border: 1px solid var(--border);
            border-radius: 12px;
            margin-bottom: 40px;
            overflow: hidden;
            background: var(--card-bg);
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        @media (min-width: 992px) {
            .product-card {
                flex-direction: row;
            }
        }
        .image-container {
            flex: 0 0 350px;
            background: #f1f2f6;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .product-image {
            width: 100%;
            height: auto;
            border-radius: 8px;
            object-fit: cover;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .product-details {
            padding: 30px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        .rank-badge {
            background: var(--primary);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 15px;
            align-self: flex-start;
        }
        .product-title {
            font-size: 1.4rem;
            color: var(--primary);
            margin: 0 0 15px 0;
            line-height: 1.4;
        }
        .product-price {
            font-size: 1.5rem;
            color: var(--accent);
            font-weight: 700;
            margin-bottom: 20px;
        }
        .analysis-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-bottom: 25px;
        }
        @media (min-width: 768px) {
            .analysis-grid {
                grid-template-columns: 1fr 1fr;
            }
        }
        .analysis-box {
            background: #f8fafc;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid var(--secondary);
        }
        .analysis-box.audience { border-left-color: #9b59b6; }
        .analysis-box.insight { border-left-color: #3498db; }
        .analysis-box.scale { border-left-color: #2ecc71; grid-column: 1 / -1; background: #f0fdf4;}
        
        .analysis-box h4 {
            margin: 0 0 10px 0;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .audience h4 { color: #8e44ad; }
        .insight h4 { color: #2980b9; }
        .scale h4 { color: #27ae60; }
        
        .analysis-box p {
            margin: 0;
            font-size: 0.95rem;
            color: #4a5568;
        }
        
        /* New Styles for Scale Images */
        .scale-section {
            margin-top: 15px;
            border-top: 1px dashed #ccc;
            padding-top: 20px;
        }
        .scale-section h4 {
            color: #d35400;
            margin-bottom: 15px;
            font-size: 1.1rem;
        }
        .scale-images-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: flex-start;
        }
        .scale-item {
            flex: 1;
            min-width: 120px;
            max-width: 180px;
            text-align: center;
        }
        .scale-item img {
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 8px;
            transition: transform 0.2s;
        }
        .scale-item img:hover {
            transform: scale(1.05);
        }
        .scale-item span {
            font-size: 0.85rem;
            color: #555;
            font-weight: 500;
        }

        .product-link {
            text-decoration: none;
            color: #fff;
            background-color: var(--secondary);
            padding: 12px 25px;
            border-radius: 6px;
            font-weight: 600;
            display: inline-block;
            align-self: flex-start;
            transition: background 0.3s;
            margin-top: 25px;
        }
        .product-link:hover {
            background-color: #2980b9;
        }
        ul {
            margin: 0;
            padding-left: 20px;
            color: #4a5568;
            font-size: 0.95rem;
        }
        li {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>Top 10 Sản Phẩm Tiềm Năng Bán Tốt Từ Macorner</h1>
        <div class="subtitle">Bao gồm Phân Tích Chuyên Sâu và 3 Hình Ảnh Gợi Ý Scale/Re-design Cho Mỗi Sản Phẩm</div>
    </div>
"""

for p in products_data:
    scale_images_html = ""
    for i in range(3):
        scale_images_html += f"""
                        <div class="scale-item">
                            <img src="{p['scale_images'][i]}" alt="Scale Idea {i+1}">
                            <span>{p['scale_labels'][i]}</span>
                        </div>
        """
        
    html_content += f"""
    <!-- Product {p['rank']} -->
    <div class="product-card">
        <div class="image-container">
            <img class="product-image" src="{p['image']}" alt="{p['title']}">
        </div>
        <div class="product-details">
            <div class="rank-badge">#{p['rank']}</div>
            <h2 class="product-title">{p['title']}</h2>
            <div class="product-price">{p['price']}</div>
            
            <div class="analysis-grid">
                <div class="analysis-box audience">
                    <h4>🎯 Tệp Khách Hàng</h4>
                    <p>{p['audience']}</p>
                </div>
                <div class="analysis-box insight">
                    <h4>💡 Phân Tích Insight</h4>
                    <p>{p['insight']}</p>
                </div>
                <div class="analysis-box scale">
                    <h4>🚀 Hướng Scale & Mở Rộng</h4>
                    <ul>
                        {p['scale']}
                    </ul>
                    
                    <!-- Scale Images Section -->
                    <div class="scale-section">
                        <h4>🎨 3 Hướng Re-design / Scale Bằng Hình Ảnh:</h4>
                        <div class="scale-images-grid">
                            {scale_images_html}
                        </div>
                    </div>

                </div>
            </div>
            <a href="{p['link']}" class="product-link" target="_blank">Xem chi tiết sản phẩm gốc</a>
        </div>
    </div>
    """

html_content += """
</div>
</body>
</html>
"""

with open("top10_products_macorner.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Đã cập nhật file HTML thành công!")
