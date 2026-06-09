import shutil
from pathlib import Path

EXCEL = 'Conil_ChatGPT.xlsx'
HTML = 'index.html'

print('=== CADIZ 2026 ===')
print('Excel encontrado:', Path(EXCEL).exists())
print('HTML encontrado:', Path(HTML).exists())
print('Base preparada para futura automatización Excel -> HTML')
