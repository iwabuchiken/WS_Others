(defun hello ()
  (print "hello, world")
  (ext:exit))

(ext:saveinitmem "hello-clisp"
                 :quiet t               ; バナーを表示しない
                 :norc t                ; 初期化ファイルをロードしない
                 :init-function #'hello ; REPLの前にhelloを呼ぶ
                 :executable t)
