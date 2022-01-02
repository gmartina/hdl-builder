# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 28/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------


import hdl_builder

def main():
    """Entry point for the application script"""
    print("Call your main application code here")
    hdl_builder.hdl_build()
    #hdl_builder.json_test()
    hdl_builder.class_test()

if __name__ == "__main__":
    main()