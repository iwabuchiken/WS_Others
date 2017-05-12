(defmacro nil! (var)
  (list 'setf var nil))

(defun add2 (n)
  (+ 2 n))
(add2 3)
