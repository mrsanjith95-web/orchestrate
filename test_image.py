from agents.image_analyzer import analyze_image

result = analyze_image(
    "images/test/sample1.jpg",
    "My laptop screen is cracked"
)

print(result)