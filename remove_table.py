import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The section to remove is:
#         <div class="single-column-v">
#           <img
#             src="../img/svg/en__table__cleaner-production__anchor-4__single-column-v-3.svg"
#             alt=""
#             data-animate="fadeInUp"
#             data-animate-delay=".6"
#           >
#         </div>

to_remove = """        <div class="single-column-v">
          <img
            src="../img/svg/en__table__cleaner-production__anchor-4__single-column-v-3.svg"
            alt=""
            data-animate="fadeInUp"
            data-animate-delay=".6"
          >
        </div>"""

if to_remove in content:
    content = content.replace(to_remove, "")
    with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Removed SVG block.")
else:
    print("Could not find the SVG block to remove.")
