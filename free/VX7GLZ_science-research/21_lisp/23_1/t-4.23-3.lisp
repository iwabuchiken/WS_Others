;; (terpri t)
;; ;;;;;;;;;;;; do-1.1 as it is ;;;;;;;;;
;; (print ";;;;;;;;;;;; do-1.1 as it is ;;;;;;;;;;;;")
;; (terpri t)

(load "quicklisp.lisp")

;; (print "quicklisp.lisp ==> loaded")

(load "C:\\Users\\iwabuchiken\\quicklisp\\setup.lisp")

;; ;(quicklisp-quickstart:install)
;;     ;; *** - Quicklisp has already been installed. Load #P"C:\\Users\\iwabuchiken\\quicklisp\\setup.lisp"
;;     ;;       instead.

;; ;(print "quicklisp-quickstart:install ===> done")

;; ;(ql:add-to-init-file)
;;     ;; *** - READ from #<INPUT BUFFERED FILE-STREAM CHARACTER #P"t-4.23-3.lisp" @16>: there is no package
;;     ;;       with name "QL"
;; ;(print "ql:add-to-init-file ===> done")

(ql:quickload "split-sequence")

;; (defun my-reverse (l &optional z)
;;   (if (atom l)
;;       z
;;       (my-reverse (cdr l) (cons (car l) z))))

;; ;(setq L1 '(1 2 3 4 5 6))
;; (setq s "Computer engineering is a discipline that integrates several fields of electrical engineering and computer science required to develop computer hardware and software.[1] Computer engineers usually have training in electronic engineering (or electrical engineering), software design, ")

;; ;(setq L1 (split-sequence:SPLIT-SEQUENCE #\Space "A stitch in time saves nine."))
;; (setq L1 (split-sequence:SPLIT-SEQUENCE #\Space s))

;; (format t "L1(before) : ~a~%" L1)


;; ;(print (my-reverse L1))
;; (setq L1-reversed (my-reverse L1))

;; (format t "L1(after) : ~a~%" L1-reversed)
;; ;(format t "L1(after) : ~a~%" (my-reverse L1))

;; (setq fname "t-4.23-3.data-1.dat")
;; (with-open-file (stream fname :direction :output)
;;   (format stream "L1 = '~a'" L1)
;;    (terpri stream)
;;    (terpri stream)
;;    (format stream "L1(reversed) = '~a'" L1-reversed))

;; (format t "file written => ~a" fname)

(terpri t)
;;;;;;;;;;;; TINK-1 &optional ;;;;;;;;;
(print ";;;;;;;;;;;; TINK-1 &optional ;;;;;;;;;;;;")
(terpri t)

(defun my-reverse (l &optional z)
;(defun my-reverse (l &key (z nil))
;  (format t "l = ~a / z = ~a~%" l z)
  (if (atom l)
      z
      (my-reverse (cdr l) (cons (car l) z));my-reverse
  );if
  );defun

(setq s " computer engineering students are allowed to choose areas of in-depth study")

(setq L1 (split-sequence:SPLIT-SEQUENCE #\Space s))

(print "L1 ==> set")

(print L1)

(setq L1-reversed (my-reverse L1))
;; &key used
;(setq L1-reversed (my-reverse L1))
    ;; *** - MY-REVERSE: keyword arguments in (("")) should occur pairwise

;(setq L1-reversed (my-reverse L1 :z nil))

(format t "L1 = '~a'~%" L1)
(format t "L1-reversed = '~a'" L1-reversed)

;(format t "s = '~a'" s)



(print "done")

;============ EOF ============
