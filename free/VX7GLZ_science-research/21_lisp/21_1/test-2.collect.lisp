;; ref http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/html/cltl/clm/node246.html
(loop for name in '(fred sue alice joe june) 
      as age in '(22 26 19 20 10) 
      append (list name age) into name-and-age-list 
      count name into name-count 
      sum age into total-age 
      finally
     (print name-count)
     (terpri t)
     (format t "result = ~a" name-and-age-list)
     (format t "round = ~d" (values (round total-age name-count))))
     
;     (format t "sum = ~d" total-age)) ;=> 'EVAL: variable TOTAL-AGE has no value'
;     (print name-and-age-list))
        ;; (return (values (round total-age name-count) 
        ;;                 name-and-age-list))) 

(terpri t)
(setq num 2)
(format t "======== SECTION : ~D =============" num)
(terpri t)
;; ref http://cl-cookbook.sourceforge.net/loop.html "until (numberp x)"
(setq line '(can also serve as a termination check 1 2 3 4))
;(loop for x in '(can also serve as a termination check 1 2 3 4)
(loop for x in line
     until (numberp x)
     collect (list x 'foo) into data
     finally
     (format t "line is : ~a" line)
     (terpri t)
     (format t "data is : ~a" data))