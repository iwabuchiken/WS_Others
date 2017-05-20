;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; setup : quicklisp
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(load "C:\\WORKS_2\\Programs\\lispbox-0.7\\quicklisp\\dists\\quicklisp\\software\\quicklisp.lisp")

(load "C:\\Users\\iwabuchiken\\quicklisp\\setup.lisp")

(ql:quickload "split-sequence")

(terpri t)
(print ";;;;;;;;;;;; EXE-1 ;;;;;;;;;;;;")
(terpri t)

(defstruct
    (bar
      (:constructor create-bar (a b))
      (:constructor create-bar-x (x &aux (a (* x 10)) (b (* x 20))))
      (:constructor create-bar-x2 (&key x))
;      (:constructor create-bar-x2 (&key x &aux (a (* x 10)) (b (* x 20))))
;      (:constructor create-bar-x2 ((x 3) &aux (a (* x 10)) (b (* x 20))))   ;=> *** - DEFSTRUCT BAR: In :CONSTRUCTOR argument list: Invalid lambda list element (X 3)
      (:constructor create-bar-y (&key x &aux (a (* x 10)) (b (* x 20))))
;		    );const
      );bar
;  (prog a b   ;=> *** - DEFSTRUCT BAR: B is not a slot option.
;  (print a)(print b)(print a*b)   ;=> *** - DEFSTRUCT BAR: (PRINT B) is not a slot option.
;  );prog
;  );defstruct
  a b);defstruct

(setq bar1 (create-bar 3 5))
(print bar1)   ;=> #<BAR :A 3 :B 5>
(print (create-bar 3 5))   ;=> #<BAR :A 3 :B 5>
;(create-bar 3 5)

(print (create-bar-x 2))
;(print (create-bar-y 2))   ;=> *** - CREATE-BAR-Y: keyword arguments in (2) should occur pairwise
(print "(create-bar-y :x 2) =>")
(print (create-bar-y :x 2))   ;=> #<BAR :A 20 :B 40>


(print "(create-bar-x2) =>")   ;=> #<BAR :A 20 :B 40>
(print (create-bar-x2))   ;=> *** - *: NIL is not a number

;(setq bar-1 (create-bar-x 2))
(print (setq bar-1 (create-bar-x 2)))

(print bar-1)

(print "(bar-a bar-1) =>")
(print (bar-a bar-1))




(print "done")
