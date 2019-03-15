# -*- mode: python -*-

block_cipher = None


a = Analysis(['U:\\PLAN\\BCUBRICH\\Python\\Ceilometer_Data\\auto_pull_MLH_from_ceilometer_LN_v1.py'],
             pathex=['C:\\Users\\bcubrich'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['PyQt5', 'dask'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='auto_pull_MLH_from_ceilometer_LN_v1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
