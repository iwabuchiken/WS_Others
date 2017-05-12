;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 
;;  smart-calc-console.lisp
;;
;; by T.Shido; Mon, 
;;
;; a simple "reverse Polish notation " 
;; pocket calculator
;; console version 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(proclaim '(inline singlep append1 strcat calc-format))

(setq *WARN-ON-FLOATING-POINT-CONTAGION* nil) ;ignore different precision

;change following values accordint to your system and your use.
(defvar *gtk-server* "C:\\bin\\gtk-server\\gtk-server.exe")
(defvar *gtk-socket* 50000)
(defvar *smart-calc-log* "smart-calc.log")
(defvar *smart-calc-constants* '((|i|   #C(0.0L0 1.0L0)) 
				 (|c|   2.99792458d8  "m s-1")   ;right speed, m s-1
				 (|h|   6.626176d-34  "J s")     ;Planc constant, J s
				 (|ec|  1.6021892d-19 "C")       ;elementary charge, C
				 (|me|  9.109534d-31  "kg")      ;electron mass, kg
				 (|u|   1.67262171d-27 "kg")     ;proton mass, kg
				 (|NA|  6.022045d23 "mol-1")     ;Avogadro constant, mol-1
				 (|k|   1.3806505d-23 "J K-1")   ;Boltzmann constant, J K-1
				 (|e|   2.7182818284590L0)))     ;Euler's constant

(defvar *smart-calc-help* '(("help"    . "show help")
			    ("const"   . "show constants")
			    ("push N"  . "add N at the beginning of the queue")
			    ("pop"     . "delete the first number of the queue")
			    ("del"     . "delete the last number of the queue")
			    ("c!"      . "clear the queue")
			    ("<"       . "call previous queue")
			    (">"       . "call next queue")
			    ("filter"  . "filter out non-numerical items")
			    ("refresh" . "refresh quene and memory windows")
			    ("mr"      . "append the memory value at the end of the queue")
			    ("mc!"     . "set the memory value 0")
			    ("bye"     . "exit from the Smart-Calc")
			    ("m+"      . "set Nm = Nm + Nq") 
			    ("m-"      . "set Nm = Nm - Nq" )
			    ("m*"      . "set Nm = Nm * Nq") 
			    ("m/"      . "set Nm = Nm / Nq")
			    (""        . "Nm and Nq are numbers of the memory and queue")))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;macros

;;; anaphoric if, the result of predition can be refered as "it"
(defmacro aif (pred then-form &optional else-form)
  `(let ((it ,pred)) (if it ,then-form ,else-form)))

;;; anapholic cond
(defmacro acond (&rest clauses)
  (if (null clauses)
      nil
      (let ((cl1 (car clauses))
            (sym (gensym)))
	(if (eq (car cl1) t)
	    `(progn ,@(cdr cl1))
	  `(let ((,sym ,(car cl1)))
	     (if ,sym
		 (let ((it ,sym)) ,@(cdr cl1))
	       (acond ,@(cdr clauses))))))))

;;; multiple-value set
(defmacro mvset(parms func)
  (let ((genparms (mapcar #'(lambda(x) (gensym (symbol-name x))) parms)))
    `(multiple-value-bind ,genparms ,func
       (setf ,@(mapcan #'(lambda(x y)  (list x y)) 
		       parms genparms)))))

;;; push and return. f, entry, queue, and calprev are captured intentionally 
(defmacro psr (vm vq)
  `(progn
     (push (cons entry queue) calprev)
     (values ,vm ,vq t entry)))

;;; define the function of '<' and '>' operator
;;; idx, calprev, and fwd are intentionaly captured
(defmacro b-f (gbf)
  (let ((q (gensym)))
    `(progn
       ,(if gbf
	    '(and (= idx 0) (not fwd)
		  (push (cons entry queue) calprev)))
       (setq fwd ,(if gbf nil t))
	  (if
	      ,(if gbf
		   '(< idx (1- (length calprev)))
		 '(< 0 idx))
	      (let ((,q  (nth
			  (,(if gbf 'incf 'decf) idx)
			  calprev)))
		(values memory (cdr  ,q) t (car ,q)))
	    (failed)))))

;;; memory, queue, and entry are captured intentionally
(defmacro failed ()
  `(values memory queue nil entry))


;;; making additional window widget with labels
(defmacro calc-show-list (ls0  lf &optional (form "~A ~A~%"))
  (let ((item (gensym)))
   `(dolist (,item ,ls0)
      (format t ,form (,(first lf) ,item) (,(second lf) ,item)))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; (mark 1)
;; examples of user defined functions
;; you can use any numerical functions 
;; without any adtional declaration.

;; calculate the value of polyniminal functions, such as f(x) = a x^3 + b x^2 + c x + d
(defun poly (x &rest parms)
  (labels ((rep (ls0 acc)
	     (if ls0
		 (rep (cdr ls0) (+ (* acc x) (car ls0)))
	       acc)))
    (rep (cdr parms) (car parms))))

;;; calculate average
(defun ave (&rest argvs)
   (/ (apply '+ argvs) (length argvs)))


;;; calculating standard devidation (SD)
;;; this SD is calculated using unbiased variance 
(defun sd (&rest argvs)
  (let ((a (apply 'ave argvs)))
    (sqrt
     (/ (apply '+ (mapcar #'(lambda (x)
			      (let ((dx (- x a)))
				(* dx dx)))
			  argvs))
	(1- (length argvs))))))

(defun stat (&rest argvs)
  (let ((av (apply 'ave argvs)))
    (values
     "N" (length argvs)
     "ave." av
     "S.D."  (sqrt
	   (/ (apply '+ (mapcar #'(lambda (x)
				    (let ((dx (- x av)))
				      (* dx dx)))
				argvs))
	      (1- (length argvs)))))))
;; (mark 2)
  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; functions
;;;
;;;flat the list

(defun singlep (lst)
  (and (consp lst) (not (cdr lst))))

(defun append1 (lst obj) 
  (append lst (list obj)))

;;; check if it is a number or a symbol bound to a number, if it is, return it.
(defun calc-number-p (s0 str0)
  (if (symbolp s0)
      (if (boundp s0)
	  (and (numberp (symbol-value s0)) s0)
	(let ((s1 (intern (delete #\Space str0))))  
	  (and (assoc s1 *smart-calc-constants* :test #'eq) s1)))
    (and (numberp s0) s0)))
	
;;; add item at the top of the queue
(defun calc-cons-p (ls0)
   (and
    (consp ls0)
    (eq (car ls0) 'push)
    (calc-number-p (second ls0) (third ls0))))

;;; memory operators, m+, m-, m*, m/
(defun calc-memoperator-p (sy0 queue memory)   
  (and
   (singlep queue)
   (aif (assoc sy0 '((m+ . +) (m- . -) (m* . *) (m/ . /)) :test #'eq)
	(let ((n (car (calc-filter queue)))
	      (op (cdr it)))
	  (or (and  (zerop n) (eq op '/)) 
	    (funcall op memory n))))))

;;;  check if the entry is numerical operators
;;;  if so, it returns a listed result.
(defun calc-operator-p (sy0 ls0)
    (and
     (symbolp sy0)
     (fboundp sy0)
     (ignore-errors
      (multiple-value-list (apply sy0 (calc-filter ls0))))))
      

;;; converts symbols to numbers
(defun calc-filter (ls0)
  (remove nil
	  (mapcar #'(lambda (x)
		      (cond
		       ((symbolp x)
			  (if (boundp x)
			      (let (( n (symbol-value x))) (and (numberp n) n))
			    (let ((v (assoc x *smart-calc-constants* :test #'eq)))
			      (and v (second v)))))
		       ((numberp x) x)
		       (t nil)))
		  ls0)))

;;; format the second and third items of elements in *smart-calc-constants*
(defun calc-fconst (ls0)
  (format nil " =  ~A ~A"
	  (calc-format (second ls0))
	  (if (cdr (cdr ls0))
	      (strcat "[" (third ls0) "]")
	    "")))
;;;
(defun calc-format (n)
  (if (complexp n)
      (format nil "[~A, ~A]" (realpart n) (imagpart n))
    (format nil "~A" n)))
;;;
(defun calc-cdr-help (ls0)
  (format nil ": ~A" (cdr ls0)))

;;; concatenate 'string
(defun strcat (&rest argvs)
  (apply #'concatenate 'string argvs))

;;;make string to show the queue
(defun calc-mstr (ls0 &optional s0 )
  (if ls0
      (calc-mstr (cdr ls0)
		 (if s0
		     (strcat s0 "  " (calc-format (car ls0)))
		   (calc-format (car ls0))))
    (or s0 " ")))   

;;; convert input string
;;;"[N,M]" --> #C(N M) and  "push N" --> (push  N "N")
(defun calc-parser (s0)
  (cond
   ((char= (char s0 0) #\[)
    (let ((p1 (position #\, s0)) (p2 (position #\] s0)))
      (if (and p1 p2)
	  (format nil "#C(~A ~A)" (subseq s0 1 p1) (subseq s0 (1+ p1) p2))
	" "))) ; dummy string
   ((and (< 5 (length s0)) (string-equal (subseq s0 0 5) "push "))
    (let ((s1 (calc-parser (subseq s0 5))))
      (format nil "(push  ~A  \"~A\")" s1 s1)))
   ((and (< 3 (length s0)) (string-equal (subseq s0 0 3) "mv "))
    (format nil "(~A)" s0))
   (t s0)))

;;; main fuction of the smart-calc
(let (calprev (idx 0) fwd)
  (defun smart-calc (memory queue entry f)
    (let ((str0 (calc-parser entry)))
      (multiple-value-bind (in y)
	  (ignore-errors (read-from-string str0))
	(or (and in  (= (length str0) y)) (return-from smart-calc (failed)))
	(format f "~A : ~S : ~A~%" memory queue entry) ;save to log
	(cond
	 ((eq in '<) (b-f t))    ;call backward queue
	 ((eq in '>) (b-f nil))  ;call forward queue
	 (t
	  (setq idx 0 fwd nil)
	  (cond
	   ((eq in 'bye)              (values nil nil 'bye nil))
	   ((eq in 'help)             (values memory queue 'help entry))
	   ((or (eq in 'const)
		(eq in 'constants))   (values memory queue 'const entry))
	   ((eq in 'filter)           (psr memory (calc-filter queue)))
	   ((eq in 'refresh)          (values memory queue t entry))
	   ((eq in 'pop)              (psr memory (cdr queue))) 
	   ((eq in 'del)              (psr memory (subseq queue 0 (1- (length queue))))) 
	   ((eq in 'c!)               (psr memory nil))  
	   ((eq in 'mc!)              (psr 0 queue))     
	   ((eq in 'mr)               (psr memory (append1 queue memory)))
	   (t
	    (acond
	     ((calc-number-p in entry)
	      (psr memory (append1 queue it)))
	     ((calc-cons-p in)
	      (psr memory (cons it queue)))
	     ((calc-memoperator-p in queue memory)
	      (psr it queue))
	     ((calc-operator-p in queue)
	      (psr memory (if (consp (car it)) (car it) it)))
	     (t                  (failed)))))))))))

;;; the main finction
(defun calc ()
  (let ((memory 0)
	(queue nil)
	(status t)
	(echo "ready"))
	    ;; the mainloop
    (with-open-file (lg *smart-calc-log* :direction :output)  ;open log file
      (format lg "memory : queue : entry~%")
      (loop
	(princ "Calc> ")
	(let ((entxt (read-line)))
	  (mvset (memory queue status echo)
		 (smart-calc memory queue entxt lg))
	  (cond
	   ((eq status 'bye) (return))
	   ((eq status 'help)
	    (calc-show-list *smart-calc-help* (car calc-cdr-help) "  ~7A ~A~%"))
	   ((eq status 'const)
	    (calc-show-list *smart-calc-constants* (first calc-fconst) "~4@A ~A~%"))
	   (t (format t "memory:[~A], echo: ~A,  status: ~A~%"
		      (calc-format memory) echo (if status "ok" "error")) 
	      (format t "queue: [~A]~%" (calc-mstr queue)))))))))
				      

				  
