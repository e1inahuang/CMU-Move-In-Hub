# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['gui.py'],
             pathex=['E:/Projects/CMU-Move-In-Hub'],
             binaries=[],
             datas=[('templates/*.html', 'templates'), ('data/*.csv', 'data')],
             hiddenimports=['flask', 'PyQt5.QtWebEngineWidgets'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='CMU_Move_In_Hub',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False) # Set `console=True` if you want a console window for debugging
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='CMU_Move_In_Hub')
