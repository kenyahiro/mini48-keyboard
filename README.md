# このキーボードについて
このキーボードは 19mmピッチ 48キーのロープロファイルキーボードです。
キースイッチは [kailh choc V1用ソケット](https://www.kailhswitch.com/mechanical-keyboard-switches/box-switches/choc-type-hot-swap-socket.html) を使用します。

マイコンには [AE-RP2040](https://akizukidenshi.com/catalog/g/g117542/) を使用します。

ファームウェアは [kmk_firmware](https://github.com/KMKfw/kmk_firmware) を使います。

# 部品表

| レフデス      | 型名           | 数量   | 備考 |
|------------|--------------|------|---------------------------|
| D1 - D48   | 1N4148W      | 48   |                           |
| SW1 - SW48 | CPG135001S30 | 48   | Choc Type Hot Swap Socket |
| U1         | AE-RP2040    | 1    | RP2040マイコンボード            |

この他に, kailh choc V1キースイッチ、 choc V1用キーキャップが必要です。
また、 基板を固定するためM2の支柱とネジを使います。


# マイコンの動作確認
組み立ての前にマイコンボードの動作確認を行います。
マイコンボードに [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) を書き込みます。

書き込み後、 [Thonny](https://thonny.org/)等でCircuitPythonが動いていることを確認します。


# 組み立て

## ダイオードのハンダ付け
はじめに, D1 - D48 のダイオードをハンダ付けします。
アノードとカソードの向きを間違えないように注意してください。

## キーソケットのハンダ付け
次にkailh choc V1用キーソケットをハンダ付けします。
キーソケットには向きがあります。 基板のシルクを参考にして、間違えないようにハンダ付けしてください。

## マイコンボードの取り付け
マイコンボードの取り付け方法は、直付け または ピンソケット の選択ができます。

直付けの場合、キーボード裏の厚みを薄くできます。しかし、マイコンボードが故障したときに交換が難しくなります。

ピンソケットを使用した場合、キーボード裏の厚みがピンソケット分増加します。マイコンボードの交換は容易です。

### マイコンボードの組み立て

マイコンボードに 細ピンヘッダ(AE-RP2040付属) または [基板用リードフレーム](https://akizukidenshi.com/catalog/g/g114883/) をハンダ付けします。

細ピンヘッダをハンダ付けする場合、 ブレッドボードを使うとハンダ付けしやすいです。

リードフレームをハンダ付けする場合、 垂直になるようにハンダ付けします。まず1ピンだけ仮止めして、角度を調整します。
垂直になったら、残りのピンをハンダ付けします。

念のため、マイコンボードの裏側に[ポリイミドテープ](https://akizukidenshi.com/catalog/r/rpolyimid/)を貼って絶縁します。


### マイコンボードの取り付け(直付けの場合)
マイコンボードの取り付け前に、ダイオードとキーソケットの向き、ハンダ不良が無いことを確認します。
特に、 マイコンボードの下になる D35, D36, SW35, SW36 は注意して確認します。

U1のスルーホールにマイコンボードを刺し込みます。マイコンボードの裏側とダイオード、キーソケットが接触していないことを確認します。

マイコンボードのハンダ付けをします。まず、1つのピンをハンダ付けして仮止めします。
マイコンボードが水平になっていることを確認します。水平でない場合、ハンダゴデで仮止めしたピンのハンダを温めて、水平になるように修正します。

仮止めでマイコンボードが水平になっていることを確認できたら、残りのピンをハンダ付けします。


### マイコンボードの取り付け(ソケットの場合)
[ピンソケット](https://akizukidenshi.com/catalog/g/g100241/)はマイコンボードのピン数に合せてカットします。

基板にピンソケットをハンダ付けします。ピンソケットは垂直になるようにハンダ付けします。まず1ピンだけ仮止めして、角度を調整します。
垂直になったら、残りのピンをハンダ付けします。