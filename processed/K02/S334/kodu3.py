news = ""
a = input("Enter first name: ")
b = input("Enter surname: ")

news = a.lower() + "." + b.lower()
if "õ" in news:
    news = news.replace('õ', 'o')
if 'ü' in news:
    news = news.replace('ü', 'u')
if 'ö' in news:
    news = news.replace('ö', 'o')
if 'ä' in news:
    news = news.replace('ä', 'a')
print(news)

