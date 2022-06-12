import glob
import json
import os
import shutil


def main():
    replace()
    os.system("newman run ./GitHubActionsPostman.postman_collection.json")
    return 0


def replace():
    postman_files = glob.glob('./postman/*.postman_collection.json')
    tar_postman_file = postman_files[0]

    with open(tar_postman_file, "r") as f:
        postman_dict = json.load(f)
        for i, var in enumerate(postman_dict["variable"]):
            if var["key"] == "todoId":
                postman_dict["variable"][i]["value"] = 1
                break

    copy_postman_file = f"./{os.path.split(tar_postman_file)[1]}"
    shutil.copy2(tar_postman_file, copy_postman_file)
    with open(copy_postman_file, 'w') as f:
        json.dump(postman_dict, f)


if __name__ == "__main__":
    main()
