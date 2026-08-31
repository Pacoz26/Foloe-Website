# -*- coding: utf-8 -*-
"""Fix contact.html: restore css/style.css + js/main.js references and strip browser-save artifacts."""
import os

PATH = r"c:\Users\zbj\Documents\Website\Foloe-Website\contact.html"

with open(PATH, "r", encoding="utf-8") as f:
    s = f.read()

# 1. Restore shared stylesheet
s = s.replace('./contact_files/style.css', 'css/style.css')
# 2. Restore shared script
s = s.replace('./contact_files/main.js.下载', 'js/main.js')
# 3. Remove live-server injected block
marker = '<!-- Code injected by live-server -->'
idx = s.find(marker)
if idx != -1:
    end = s.rfind('</script>')
    s = s[:idx] + s[end + len('</script>'):]

# 4. Normalize trailing whitespace before </body>
import re
s = re.sub(r'\n{3,}</body></html>\s*$', '\n</body>\n</html>\n', s)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(s)

print("done. remaining contact_files refs:", s.count('contact_files'))
