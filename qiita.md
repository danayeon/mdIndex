# 目次
 1. npm ERR! Cannot read property 'match' of undefined
 1. パッケージのバージョン管理
  1.  バージョンの確認
  1.  npm-check-updatesが便利
 1. npm audit
 1. Error: Cannot find module 'webpack-cli/bin/config-yargs'
 1. compilation.mainTemplate.applyPluginsWaterfall is not a function

Vue.jsでの開発を行う上で遭遇したエラー等について得た情報のまとめ



# npm ERR! Cannot read property 'match' of undefined
`npm install`を行った際に遭遇
`package-lock.json`とのズレがあると起こるらしいので`package-lock.json`を消してやると解決
### 参照ページ
https://qiita.com/mojirico/items/8db742fa5f22e3e719c4
https://www.nekoni.net/Blog/Article/npm-err-cannot-read-property-match-of-undefined

# パッケージのバージョン管理
## バージョンの確認
通常

```bash:terminal
npm list --depth=0 # インストール済みの全てのパッケージ

npm outdated # 古くなったパッケージ
# 各列の意味
# Current => 現在インストールされているバージョン
# Wanted  => package.jsonのsemverを満たす最新のバージョン
# Latest  => 最新バージョン
```

## npm-check-updatesが便利

```bash:terminal
npm install -g npm-check-updates # インストール

ncu # 現在のバージョンと最新バージョン
ncu -u # package.jsonの更新
ncu -a # マイナーバージョン以下アップデートについても更新
```
### 参照ページ
https://dackdive.hateblo.jp/entry/2016/10/10/095800

# npm audit
`npm install`時などに脆弱性を警告されたパッケージについての処理
1. `npm audit`で脆弱性のあるパッケージを一覧表示
2. `npm i [パッケージ名] -D`で修正済みパッケージをインストール
3.  `npm ls [パッケージ名]`でパッケージの依存関係を確認
4. 上記実行時に`deduped`を表記されているパッケージを削除(FinderでもOK)
5. `npm dedupe`で依存関係を整理

package.jsonの更新を自動化すればもっと楽らしい

### 参照ページ
https://qiita.com/hibikikudo/items/0af352acac85fce28ec2

# Error: Cannot find module 'webpack-cli/bin/config-yargs'
`sass-loader`等を使い始めてから`npm run dev`で吐かれたエラー
`webpack`、`webpack-cli`、`webpack-dev-server`のバージョンの組み合わせの問題らしい
全て最新版をインストール

```bash:terminal
npm isntall --save-dev webpack@latest # webpack

npm install webpack-cli -D # webpack-cli

npm isntall --save-dev webpack-dev-server@latest # webpack-dev-server

npm install vue-loader@latest # vue-loader
```

### 参照ページ
https://qiita.com/Shoryu_N/items/9ae2417489c9faaa271c

# compilation.mainTemplate.applyPluginsWaterfall is not a function
パッケージの脆弱性を解決すると消えた

### 参照ページ
https://qiita.com/mitsuya_bauhaus/items/c31b146fb9649469f8d1
