from tools3.compile.uc import CompileUC

def uc_gen_cases(compile_json_file_path, fields, expected, include_field_names=False, separator="_"):
    compile_uc = CompileUC(
        fields=fields,
        expected=expected,
        include_field_names=include_field_names,
        separator=separator,
    )
    return compile_uc.compile(compile_json_file_path)