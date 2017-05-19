(terpri t)
;;;;;;;;;;;; TINK-2 &key ;;;;;;;;;
(print ";;;;;;;;;;;; TINK-2 &key ;;;;;;;;;;;;")
(terpri t)

;; ref http://www.geocities.jp/m_hiroi/xyzzy_lisp/abclisp06.html "&key で指定された引数"
; &key の使用例
(write
 ((lambda (a &key b c) (list a b c));lambda
 10);=> (10 NIL NIL)
)

(terpri t)
; デフォルト値の指定
(write
 (
  (lambda (a &key (b 1) (c 2)); param
     (list a b c); operation
     );lambda
  10 :c 22   ;=> (10 1 22)
;  10   ;=> (10 1 2)
;  10 :c 20 :b 30 ;args   ;=> (10 30 20)
  );(
);write

(terpri t)
;;;;;;;;;;;; TINK-3 &optional ;;;;;;;;;
(print ";;;;;;;;;;;; TINK-3 &optional ;;;;;;;;;;;;")
(terpri t)

(write
 (
  (lambda
       (a &optional (b 10)) ;params
     (+ a b) ;ops
     );lambda
  1)   ;=> 11
;   1 2);(   ;=> 3
);write


;; (terpri t)
;; ;;;;;;;;;;;; SEG-1 example ;;;;;;;;;
;; (print ";;;;;;;;;;;; SEG-1 example ;;;;;;;;;;;;")
;; (terpri t)

;; (defun test (x)
;;   (format t "arg is '~a'" x))
;; (test "aaa")

;; (defun my-reverse (l)
;;   (print l))
;; ;(my-reverse "xxxx")   ;=> "xxxx"
;; (my-reverse
;;  (make-sequence
;;   'string 5
;;   :initial-element #\r))   ;=> "rrrrr"

;; (defun my-reverse (l)
;;   ;;; ref atom https://www.tutorialspoint.com/lisp/lisp_predicates.htm
;;   (if (atom l)
;;       l
;;       (append (my-reverse (cdr l)) (list (car l)));append
;;       );if
;;   );defun

;; (terpri t)
;; (write-line "defun => done: my-reverse")

;; (write
;;  (
;;   (my-reverse (list 'a 'b 'c))
;;   );(
;;  );write


;; (write
;;  (
;;   (my-reverse 'abcde)
;;   );(
;;  );write
;;    ;=> *** - EVAL: (MY-REVERSE 'ABCDE) is not a function name; try using a symbol instead

;; (write
;;  (
;;   (my-reverse '(a b c d))
;;   );(
;; );write
;;    ;=> *** - EVAL: (MY-REVERSE '(A B C D)) is not a function name; try using a symbol instead

(terpri t)
;;;;;;;;;;;; SEG-1.TINK-1 (defun my-dev  ;;;;;;;;;
(print ";;;;;;;;;;;; SEG-1.TINK-1 (defun my-dev ;;;;;;;;;;;;")
(terpri t)

;; (defun my-rev (l)
;;   l)

;; (print (my-rev '(a b c d e)))   ;=> (A B C D E)
;; (defun my-rev (l)   ; version 1.1
;;   (if (atom l)
;;       l
;;       (print "not atom")
;;       );if
;;   );defun

;; (print (my-rev '(a b c d e)))   ;=> "not atom"

;; (defun my-rev (l)   ; version 1.2
;;   (if (atom l)
;;       l
;;       ;; ref progn http://www.haun.org/kent/lisp1/1.html
;;       (progn
;;       (print "not atom")
;;       (my-rev (cdr l));my-rev
;;       );progn
;;       );if
;;   );defun

;; (print (my-rev '(a b c d e)))   ;=>
;; ;; "not atom"
;; ;; "not atom"
;; ;; "not atom"
;; ;; "not atom"
;; ;; NIL

;; (defun my-rev (l)   ; version 1.2
;;   (if (atom l)

;;       (progn
;; 	;(print "is atom")
;; 	(format t "is atom : ~a" l)
;; 	l
;; 	);progn

;;       (progn
;;       ;(print "not atom  : ~a" l)
;;         (format t "not atom : ~a~%" l)
;;       (my-rev (cdr l));my-rev
;;       );progn
;;       );if
;;   );defun

;; (setq L1 '(a b c d e))
;; (print (my-rev L1))   ;=>
;; ;(print (my-rev '(a b c d e)))   ;=>

(terpri)
(print "version 1.3")
(terpri)

(defun my-rev (l)   ; version 1.3
  (if (atom l)

      (progn
	;(print "is atom")
	(format t "is atom : ~a" l)
	l
	);progn

      (progn
      ;(print "not atom  : ~a" l)
	;; ref multiple lines http://stackoverflow.com/questions/16846515/multi-line-documentation-strings-in-lisp "answered May 31 '13 at 0:31"
        (format t "not atom : ~a / cdr = ~a ~
                   / car = ~a / (list (car)) = ~a~%"
		l (cdr l) (car l) (list (car l)))
	(append
	    (my-rev (cdr l))
	    (list (car l))
	 );append
;      (my-rev (cdr l));my-rev
      );progn
      );if
  );defun

(setq L1 '(a b c d e))
(format t "L1 => ~a~%" L1)
;(print L1)
(print (my-rev L1))   ;=>


;============ EOF ============
