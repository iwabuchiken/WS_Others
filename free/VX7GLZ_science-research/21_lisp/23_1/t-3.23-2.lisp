(terpri t)
;;;;;;;;;;;; EXE-1 my-rev-sub ;;;;;;;;;
(print ";;;;;;;;;;;; EXE-1 my-rev-sub ;;;;;;;;;;;;")
(terpri t)

(setq abc 1)

(defun my-rev-sub (l z)
  (format t "l is ~a, z is ~a~%" l z)
  (if (atom l)
      (progn
	(format t "l is atom (~a) : ~a~%" l z)
	z
	
      );progn

      (progn
	(format t
		"l = ~a / (cdr l) = ~a ~
                  / (car l) = ~a ~
                 / (cons (car l) z) = ~a ~
                  ~%"
		l (cdr l) (car l) (cons (car l) z))
	;; (format t (
	;; 	   "l = ~a / (cdr l) = ~a / (car l) = ~a ~
        ;;             (cons (car l) z) = ~a ~
        ;;            ~%")
	;; 	   l (cdr l) (car l) (cons (car l) z));format
      (my-rev-sub (cdr l) (cons (car l) z));(my-rev...
;      (print (my-rev-sub (cdr l) (cons (car l) z)));(my-rev...
;      (terpri t)
;      (format t "(my-rev-sub ==> done~%")
;      (format t "(my-rev-sub ==> done (~d) ~%" abc)
;      (setq abc (+ abc 1))

      );progn

      );if
  )

(defun my-reverse (l) (my-rev-sub l nil))

(setq L1 '(1 2 3 4))
(print L1)
(terpri t)
(print (my-reverse L1))

   ;; (1 2 3 4)
   ;; l is (1 2 3 4), z is NIL
   ;; l = (1 2 3 4) / (cdr l) = (2 3 4) / (car l) = 1 / (cons (car l) z) = (1)
   ;; l is (2 3 4), z is (1)
   ;; l = (2 3 4) / (cdr l) = (3 4) / (car l) = 2 / (cons (car l) z) = (2 1)
   ;; l is (3 4), z is (2 1)
   ;; l = (3 4) / (cdr l) = (4) / (car l) = 3 / (cons (car l) z) = (3 2 1)
   ;; l is (4), z is (3 2 1)
   ;; l = (4) / (cdr l) = NIL / (car l) = 4 / (cons (car l) z) = (4 3 2 1)
   ;; l is NIL, z is (4 3 2 1)
   ;; (my-rev-sub ==> done (1)
   ;; (my-rev-sub ==> done (2)
   ;; (my-rev-sub ==> done (3)
   ;; (my-rev-sub ==> done (4)

   ;; 5


;============ EOF ============
