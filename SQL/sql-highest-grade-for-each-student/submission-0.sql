-- Write your query below

WITH cte1 AS
(
    SELECT student_id, MAX(score) as max_score
    FROM exam_results
    GROUP BY student_id
)
SELECT DISTINCT ON (exam_results.student_id)
    exam_results.student_id, exam_results.exam_id, exam_results.score
FROM exam_results
LEFT JOIN cte1
ON exam_results.student_id = cte1.student_id
WHERE score = max_score
ORDER BY student_id