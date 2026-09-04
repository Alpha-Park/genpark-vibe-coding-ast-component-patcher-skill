from client import VibeCodingAstComponentPatcherClient

def main():
    client = VibeCodingAstComponentPatcherClient()
    res = client.patch_react_component()
    print('AST Component Patcher: ' + res['patch_run_id'] + ' (' + res['component_name'] + ')')
    print('Parsed: ' + str(res['jsx_ast_parsed_cleanly']) + ' | Tailwind Added: ' + str(res['tailwind_classes_appended']))
    print('Diff URL: ' + res['patch_diff_url'])

if __name__ == '__main__':
    main()
