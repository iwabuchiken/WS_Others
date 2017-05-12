(setq num (+ 4 5))
(write num)
(write-line "")

(defmacro setTo10 (num)
  (setq num 10)
  (write-line "changing the value...")
  (print num))

(write-line "num is now ")
;(print "num is now ")
;(print 'num is now ')
(print num)
(format t "~%")
;(write-line "")

(setq x 10)
(setq y 20)
(format t "x = ~2d y = ~2d ~%" x y)

;;ref https://www.tutorialspoint.com/lisp/lisp_variables.htm "(let ((x 'a)"
;;;;; let ---> local variable
(let ((x 'a) (y 'b)(z 'c))
(format t "x = ~a / y = ~a / z = ~a" x y z))
;(format t "x = ~a / y = ~a / z = ~a" x y z)

(write "")
(write-line "using ---> setq")
;(setq ((x 'a) (y 'b)(z 'c))   ;=> 'SETQ: ((X 'A) (Y 'B) (Z 'C)) is not a symbol'
(setq x 'a)
(setq y 'b)
(setq z 'c)
(format t "x = ~a / y = ~a / z = ~a" x y z)
;(format t "x = ~a / y = ~a / z = ~a~%" x y z)

;;;ref http://stackoverflow.com/questions/2619172/common-lisps-equivalent-of-r-inside-the-format-function answered Apr 14 '10 at 20:40
;(format t "~CHello world.~C~C" #\return #\return #\linefeed)
;(format t "Hello world.~C~C" #\return #\linefeed)
(format t "Hello world.~C" #\return)

(write-char #\return)
;;;ref https://www.tutorialspoint.com/lisp/lisp_variables.htm
(prog ((x '(a b c))(y '(1 2 3))(z '(p q 10)))
(format t "x = ~a y = ~a z = ~a" x y z))

;(print (first x))   ;=> 'FIRST: A is not a list'

(print x)
;(write-line x)   ;=> 'WRITE-LINE: argument A is not a string'

;;;;;ref https://www.tutorialspoint.com/lisp/lisp_constants.htm
(defconstant PI 3.141592)
(defun area-circle(rad)
   ;;;ref https://forums.autodesk.com/t5/visual-lisp-autolisp-and-general/what-is-terpri/td-p/1822075
   (terpri)
   (terpri)
   (format t "Radius: ~5f" rad)
   (format t "~%Area: ~10f" (* PI rad rad)))
(area-circle 10)

;;;ref https://www.tutorialspoint.com/lisp/lisp_file_io.htm "Example 1"
;(with-open-file (stream "/tmp/myfile.txt" :direction :output)

(setq fname "sub1.data")
(print fname)
(terpri)

;(with-open-file (stream "myfile.txt" :direction :output)
(with-open-file (stream fname :direction :output)
   (format stream "Welcome to Tutorials Point!")
   (terpri stream)
   (format stream "This is a tutorials database")
   (terpri stream)
   (format stream "Submit your Tutorials, White Papers and Articles into our Tutorials   Directory.")
)

(write-line "file written")

