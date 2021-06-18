isValid :: String -> Bool
isValid "" = True
isValid (first:rest) = rec (first:rest) ""
    where
        rec :: String -> String -> Bool
        rec "" stack = null stack
        rec (f:r) stack | f `elem` "({[" = rec r (f:stack)
                        | null stack    = False
                        | otherwise     = op (head stack) == f && rec r (tail stack)

        op :: Char -> Char
        op '(' = ')'
        op '{' = '}'
        op '[' = ']'
