import os

assets = os.path.dirname(os.path.abspath(__file__)) + "/assets"
cwd = os.getcwd()

COMMAND=f"cat {assets}/passwd | MY_LINE1=24 MY_LINE2=42 sh r_tacpy.sh"
OUTPUT="""
z_iew, z_idauoj, z_hcinh, z_habsem_ante, z_guomah, z_girdor, z_farhca, z_evuohc, z_ettorb, z_etset, z_etanok, z_elliap, z_ehkuob, zeek, zdud, z_dnarud, z_dahuob, z_cdadah, z_azhral_ante.
"""
