import os


def read_links_file(links_file_path):
    """
    Reads the links file and returns a list of download tasks.
    Each task is a dictionary containing the link, name, and folder name.
    """
    if not os.path.exists(links_file_path):
        raise FileNotFoundError(f"Links file not found: {links_file_path}")

    tasks = []
    folder_name = None

    with open(links_file_path, "r") as links_file:
        for line in links_file:
            line = line.strip()
            if not line:
                continue

            # Check if the line specifies the folder name
            if line.startswith("folder:"):
                folder_name = line.split("folder:")[1].strip()
                continue

            # Ensure a folder name has been set
            if not folder_name:
                print("Skipping links because no folder name is specified.")
                continue

            # Parse the link and name
            parts = line.split()
            if len(parts) != 2:
                parts.append("")
                # print(f"Skipping invalid line: {line}")
                # continue

            link, name = parts
            tasks.append({"link": link, "name": name, "folder_name": folder_name})

    return tasks
