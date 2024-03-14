#! /usr/bin/env python3

import re
import argparse

from pathlib import Path

CSS_IN_JS_REGEX = r"(?:const )?([a-zA-z]+) = css`([^`]+)`;"
IMPORT_REGEX = r"import[^;]+;"


def get_import_list(js):
    return re.findall(IMPORT_REGEX, js)


def strip_css_in_js_declarations(js):
    return re.sub(CSS_IN_JS_REGEX, "", js)


def insert_styles_import(refactored_js, component_name):
    import_list = get_import_list(refactored_js)
    end_of_imports = refactored_js.find(import_list[-1]) + len(import_list[-1])
    refactored_js = (
        refactored_js[:end_of_imports]
        + f"\nimport * as styles from './{component_name}.module.css'\n"
        + refactored_js[end_of_imports:]
    )
    return refactored_js


def main(args):
    js_path = Path(args.file)
    component_name = js_path.stem
    with js_path.open() as js_file:
        js = js_file.read()
    css_in_js = re.findall(CSS_IN_JS_REGEX, js)

    refactored_js = strip_css_in_js_declarations(js)
    refactored_js = insert_styles_import(refactored_js, component_name)

    with open(f"./{component_name}.module.css", "w") as css_module:
        for class_name, css in css_in_js:
            new_class_name = input(f"Rename {class_name} to: ")
            if new_class_name:
                refactored_js = refactored_js.replace(
                    class_name, f"styles['{new_class_name}']"
                )
                class_name = new_class_name
            css_module.write(".{} {{ {} }}\n\n".format(class_name, css))

    with open(f"./{component_name}_updated.js", "w") as rewritten_js:
        rewritten_js.write(refactored_js)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="file", required=True)

    args = parser.parse_args()
    main(args)
