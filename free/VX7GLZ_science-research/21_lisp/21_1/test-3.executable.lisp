(defun hello ()
  (print "hello, world")
  (ext:exit))

(ext:saveinitmem "hello-clisp"
                 :quiet t               ; �o�i�[��\�����Ȃ�
                 :norc t                ; �������t�@�C�������[�h���Ȃ�
                 :init-function #'hello ; REPL�̑O��hello���Ă�
                 :executable t)
