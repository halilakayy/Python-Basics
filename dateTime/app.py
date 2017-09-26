from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "")
print(datetime.now().strftime("%D"))
print(datetime.now().strftime("%d %B %Y"))