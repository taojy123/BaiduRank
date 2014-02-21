# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'App1.py'],
             pathex=['C:\\Users\\TJY\\Desktop\\BaiduRank'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'BaiduRank.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
