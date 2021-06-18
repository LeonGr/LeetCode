merge :: [Int] -> [Int] -> [Int]
merge xs ys = recMerge [] xs ys
    where
        recMerge :: [Int] -> [Int] -> [Int] -> [Int]
        recMerge as [] ys = as ++ ys
        recMerge as xs [] = as ++ xs
        recMerge as (x:xs) (y:ys)
          | x > y  = recMerge (as ++ [y]) (x:xs) ys
          | x <= y = recMerge (as ++ [x]) xs     (y:ys)
