import traceback

def execute_code(code):
    try:
        exec(code,{},{})
        return ({"status":"success", "message": "Code executed successfully"})
    
    except Exception as e:
        return {
            "status":"error",
            "error_message": str(e),
            "traceback": traceback.format_exc()
        }