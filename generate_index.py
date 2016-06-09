import glob
import os
def get_yml_data(files, prefix="  ", file_prefix = ""):
	res = ""
	for i in files:
		with open(i) as mdfile:
			title_line = mdfile.readline().split("# ")[1].split("]")[0].replace("[","") + ")"
			res += "{}- {}: {}{}\n".format(prefix, title_line, file_prefix, os.path.basename(i))
	return res

def get_index_data(files, file_prefix = ""):
	res = ""
	for i in files:
		with open(i) as mdfile:
			title_line = mdfile.readline().split("# ")[1].split("]")[0].replace("[","") + ")"
			res += "[{}]({}{})\n\n".format(title_line, file_prefix, os.path.basename(i))
	return res
yml = ""
md_done = ""
md_todo = ""
for i in range(7,-1,-1):
	i_str = str(i)
	form = "docs/{}?.md".format(i)

	yml_tmp = get_yml_data(glob.glob(form))
	if yml_tmp != "":
		yml += "- {0}0 - {0}9:\n".format(i)
		yml += yml_tmp


	md_tmp = get_index_data(glob.glob(form))
	if md_tmp != "":
		md_done += "## Folge {0}0 - {0}9\n\n".format(i)
		md_done += md_tmp
yml += "- Todo:\n"
for i in range(7,-1,-1):
	i_str = str(i)
	form = "docs/todo/{}?.md".format(i)

	yml_tmp = get_yml_data(glob.glob(form), "    ", "todo/")
	if yml_tmp != "":
		yml += "  - {0}0 - {0}9:\n".format(i)
		yml += yml_tmp


	md_tmp = get_index_data(glob.glob(form), "todo/")
	if md_tmp != "":
		md_todo += "### Folge {0}0 - {0}9\n\n".format(i)
		md_todo += md_tmp

with open("mkdocs.yml.template") as tmpfile:
	data = tmpfile.read()
	data = data.replace("{{ PAGES }}", yml)
	with open("mkdocs.yml", "w") as outfile:
		outfile.write(data)


with open("docs/index.md.template") as tmpfile:
	data = tmpfile.read()
	data = data.replace("{{ EXPERIMENTE }}", md_done)
	data = data.replace("{{ TODO }}", md_todo)
	with open("docs/index.md", "w") as outfile:
		outfile.write(data)