CellularAutomata to generate test pattern for "Dream by Fetus Project"(DbFP)
「胎児の見る夢」プロジェクト(DbFP)のためのテストパターン生成のためのcellular automata。 

Python / numpy / matplotlibで書かれている。

DbFPは胎児の時にも網膜に近いところで光が無くてもパターンを生成していて、それにより視神経ネットワークとその上位の神経ネットワークの学習を促進・調節・補正しているのではないか、という考えに基づき、テストパターンをcellular automataなどで生成して、それを学習していないCNNなどに入力することにより、一般の画像認識の学習の最適化が短縮される、というようなことがあるかどうか調べる試み。

まず、最初のコードはランダムに0-255までの値の二次元画像を作成し、ひとつのピクセルを中心とした9つのピクセルの値を平均したものが、127.5以上ならば、中心のピクセルにupの値を加算し、逆ならば down(マイナス)の値を足すことで、値を減らす、ということを繰り返す、cellular automataになっている。

![alt text]https://github/sumi-yaki/CellularAutomata/blob/master/anime.gif)
