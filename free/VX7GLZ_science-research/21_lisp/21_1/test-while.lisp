;ref http://www.geocities.jp/m_hiroi/xyzzy_lisp/abclisp04.html
;(loop
 ;  for x in '(a b c d e)
;
 ;    do (print x)
;
;)


;;;ref http://cl-cookbook.sourceforge.net/loop.html
(loop for x in '(a b c d e)
     for y in '(1 2 3 4 5)
     ;ref http://www.geocities.jp/m_hiroi/xyzzy_lisp/abclisp07.html "書式文字列の中には、変換指示子"
     do (format t "(~a and ~a)" x y))
;     do (list x y))   ;=> no output
;   do (collect (list x y)))   ;=> '- EVAL: undefined function COLLECT'
;     do (format t "~a ~a" x y))   ;=> works.
;     (format t "~a ~a" x y))   ;=> n.w.
;     collect (list x y))   ;=> n.w.

(terpri t)
;(print "=========== SECTION : 2 =================")
(setq num 2)
;(setq num '2)
(format t "======== SECTION : ~D =============" 2)
;;;ref http://cl-cookbook.sourceforge.net/loop.html"Iterate using a counter, and a variable whose "
;(print num)
; example : 1
(loop for x from 1 to 5
     do (print x)) 
; example : 2
(loop
     for x from 1 to 5
     for y = (* x 2)
   ;     do (format t "x = ~d / y = ~d / (* x 2) = ~d ||" x y (* x 2)))   ;=> w.
    do
     (format t "x = ~d / y = ~d / (* x 2) = ~d ||" x y (* x 2))
     (terpri t)
     );loop

;;;ref http://www.geocities.jp/m_hiroi/xyzzy_lisp/abclisp07.html
;(format t "１０進数表示 ~D" 256)

;;;ref "Iterate through a list, and have a counter iterate in parallel"
(loop
     for x in '(a b c d e)
     for y from 1

     when (> y 3)
     do (format t "y is larger than 3: ~d" y)
        (terpri t)

     do (format t "y is NOT YET > 3 : ~d" y)
        (terpri t)

     do (format t "y = ~d / x = ~a" y x)
        (terpri t))
     ;; do (format t "y = ~d / x = ~a" y x)
;;    (terpri t))
;; 
;     when (> y 1)
 ;    do (format t ",")
  ;   do (format t "~a" x))
;; 

(setq num 3)
(format t "======== SECTION : ~D =============" num)
(terpri t)
;; ref http://cl-cookbook.sourceforge.net/loop.html "Terminate the loop early using a test."
(loop for x in '(a b c d e 1 2 3 4)
     until (numberp x)
     collect (list x 'foo))
     ;; (format t "is number => '~d'" x)) ;=> 'LOOP: illegal syntax near'
     ;; do
     ;; (format t "x is ~a" x)
     ;; (terpri t)
     ;)

(setq num 4)
(format t "======== SECTION : ~D =============" num)
(terpri t)
(loop for x in '(a b c d e)
     (format t "x = '~a'" x)
     collect x into data
     finally
     (return (values (data))))
