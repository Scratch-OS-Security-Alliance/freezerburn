from json import load, dump

def patchProjectJSON(filepath: str) -> None: 
    # List of sprites that may potentially trigger the anticheat
    culprits = [
        'pear-anticheat-v2',
        'detector',
        'report detector',
    ]

    with open(filepath, "r") as f:
        try:
            project = load(f)
            sprites = project['targets']
            print("Browsing project.json...")
        except TypeError:
            print("[ERROR] Could not load project.json!")

    if type(project) == dict:
        for i in sprites:
            if i['name'] in culprits:
                print(f"Culprit found: `{i['name']}`. Removing...")
                sprites.remove(i)
        project['targets'] = sprites
        with open(filepath, "w") as f:
            print("Saving project.json...")
            dump(project, f, indent=None)
    else:
        print("[ERROR] Could not recognice file structure.")