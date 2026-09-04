class VibeCodingAstComponentPatcherClient:
    def patch_react_component(self, component_code='export function Card() { return <div className="p-4">Old</div>; }', patch_directive='Add dark mode background and rounded corners'):
        return {
            'patch_run_id': 'ast_ptc_9918',
            'component_name': 'Card',
            'patched_code': 'export function Card() { return <div className="p-4 bg-white dark:bg-slate-900 rounded-xl shadow-sm">Old</div>; }',
            'jsx_ast_parsed_cleanly': True,
            'syntax_errors_count': 0,
            'tailwind_classes_appended': ['bg-white', 'dark:bg-slate-900', 'rounded-xl', 'shadow-sm'],
            'patch_diff_url': 'https://lovable.ast.genpark.ai/diffs/9918.diff'
        }
