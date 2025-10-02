from database.connection import db

crop_info_collection = db["crop_info"]

crop_data = [
    {"crop": "apple", "reason": "Requires cool climate with good chilling hours.", "sowing_period": "December to February", "tip": "Plant in well-drained loamy soil with adequate sunlight."},
    {"crop": "banana", "reason": "Prefers high humidity and rich soil.", "sowing_period": "June to August", "tip": "Use drip irrigation and provide windbreaks."},
    {"crop": "black gram", "reason": "Grows well in warm weather and well-drained soil.", "sowing_period": "June to July", "tip": "Apply rhizobium culture to boost yield."},
    {"crop": "chickpea", "reason": "Thrives in cooler season with moderate rainfall.", "sowing_period": "October to November", "tip": "Avoid waterlogging and use raised beds."},
    {"crop": "coffee", "reason": "Requires humid climate and shade.", "sowing_period": "June to September", "tip": "Plant under shade trees and ensure regular pruning."},
    {"crop": "coconut", "reason": "Grows well in coastal humid climate.", "sowing_period": "June to July", "tip": "Maintain proper drainage to avoid root rot."},
    {"crop": "cotton", "reason": "Needs dry climate and black soil.", "sowing_period": "April to May", "tip": "Ensure pest control, especially for bollworms."},
    {"crop": "grapes", "reason": "Prefers dry and warm climate.", "sowing_period": "January to February", "tip": "Provide support with trellises and prune regularly."},
    {"crop": "jute", "reason": "Requires high rainfall and nitrogen-rich soil.", "sowing_period": "March to May", "tip": "Avoid waterlogging and maintain spacing."},
    {"crop": "kidneybeans", "reason": "Grow best in cool temperatures with fertile soil.", "sowing_period": "October to November", "tip": "Ensure adequate spacing and pest monitoring."},
    {"crop": "lentil", "reason": "Needs moderate rainfall and cool weather.", "sowing_period": "November to December", "tip": "Use certified seeds to ensure high germination."},
    {"crop": "maize", "reason": "Thrives in fertile soil with moderate moisture.", "sowing_period": "June to July", "tip": "Plant in rows and use nitrogen-rich fertilizers."},
    {"crop": "mung bean", "reason": "Grows well in warm, dry weather.", "sowing_period": "June to July", "tip": "Use well-drained soil and avoid excessive watering."},
    {"crop": "moth beans", "reason": "Suitable for dry regions with sandy soil.", "sowing_period": "July to August", "tip": "Great for intercropping; requires minimal inputs."},
    {"crop": "muskmelon", "reason": "Needs hot and dry weather with loamy soil.", "sowing_period": "February to March", "tip": "Ensure mulching and proper pollination."},
    {"crop": "orange", "reason": "Requires subtropical climate and light soil.", "sowing_period": "July to August", "tip": "Apply micronutrients like zinc and iron regularly."},
    {"crop": "papaya", "reason": "Grows fast in warm and humid climate.", "sowing_period": "March to April", "tip": "Ensure good drainage and remove male plants."},
    {"crop": "pigeon peas", "reason": "Ideal for rainfed conditions and deep soil.", "sowing_period": "June to July", "tip": "Use treated seeds and avoid water stagnation."},
    {"crop": "pomegranate", "reason": "Thrives in dry and semi-arid climate.", "sowing_period": "February to March", "tip": "Do pruning post-harvest and use organic mulching."},
    {"crop": "rice", "reason": "Requires standing water and high humidity.", "sowing_period": "June to July", "tip": "Use transplanting for better yield."},
    {"crop": "watermelon", "reason": "Prefers sandy loam soil and hot weather.", "sowing_period": "January to March", "tip": "Avoid overhead irrigation; use drip instead."},
    {"crop": "mango", "reason": "Grows best in tropical climate with good drainage.", "sowing_period": "July to August", "tip": "Apply potash and prune after harvest."}
]

# Clear existing and insert fresh
crop_info_collection.delete_many({})
crop_info_collection.insert_many(crop_data)
print("🌾 All crop info inserted successfully!")
