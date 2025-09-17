###########- currently working on this file
from model import add_link, get_links, get_link, edit_link, delete_link, list_groups , count_in_group

format_groups = lambda groups: "\n".join(f"• {g}" for g in groups)
format_links = lambda links: "\n".join(f"[{l['id']}] {l['title']} ({l['url']})" for l in links)
format_links_group = lambda links: "\n".join(f"[{l['id']}] -|{l['groupe']}|- {l['title']} ({l['url']})" for l in links)

'''
commands = {
    "add": addLink
    "edit": editLink
    "delete": delLink
}
'''

def is_found(link_id):
    item = get_link(link_id)
    if (item != None):
        #return item
        return True
    else:
        #return f"404 - Id '{link_id}' not found."
        return False

while True:
    print("""\nType one of the options bellow: \n\n-- add/+:\tcreate a new link element\n-- edit:\tmodify an existing link element\n-- delete/-:\tremove an existing link element\n-- links:\tdisplays existing link elements\n-- link:\tdisplays one existing link element\n-- groups:\tdisplays existing group of link element\n""")
    command = input(">")

    if (command.strip().lower() in ["exit", "quit"]):
        exit()

    if (command.strip().lower() in ["add", "+"]):
        url = input("> URL: ")
        title = input("> Title: ")
        details = input("[Leave empty if needed]\n> Details(optional): "); details = details.strip() or None
        print(f"---------------\nExisiting groups ( case sensitive ):\n{format_groups(list_groups())}\n---------------\n")
        group = input ("[Leave empty to set as GLOBAL]\n> Groupe: "); group = group.strip() or 'GLOBAL'

        print(add_link(title, url, details = details, group = group))
        continue
    if (command == "edit"):
        id = input("> id: ")
        if is_found(id):
            link = get_link(int(id))
            print(f"\nOld URL - {link['url']}\n")
            url = input("> New URL: ")
            print(f"\nOld Title - {link['title']}\n")
            title = input("> New Title: ")
            print(f"\nold Details - {link['details']}\n")
            details = input("[Leave empty if needed]\n> New Details(optional): "); details = details.strip() or None
            print(f"\nold Group - {link['groupe']}\n")
            print(f"---------------\nExisiting groups ( case sensitive ):\n{format_groups(list_groups())}\n---------------\n")
            group = input ("[Leave empty to set as GLOBAL]\n> New Groupe: "); group = group.strip() or 'GLOBAL'
            print(edit_link(id, title, url, details = details, group = group))
        else:
            print(f"---------------\n[{id}] -|404|- NOT FOUND\n---------------")
        continue
    
    if (command.strip().lower() in ["delete", "-"]):
        id = input("> id: ")
        if is_found(id):
            #link = get_link(int(id))
            print(delete_link(id))
        else:
            print(f"---------------\n[{id}] -|404|- NOT FOUND\n---------------")
        continue
    if (command == "link"):
        id = input("> id: ")
        if is_found(id):
            link = get_link(int(id))
            print(f"---------------\n{format_links_group([link])}\n---------------")
        else:
            print(f"---------------\n[{id}] -|404|- NOT FOUND\n---------------")
        continue

    if (command == "links"):
        print(format_links(get_links()))
        continue

    if (command == "groups"):
        print(f"---------------\nExisiting groups:\n{format_groups(list_groups())}\n---------------\n")