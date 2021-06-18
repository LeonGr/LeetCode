use std::collections::HashSet;

fn contains_duplicate(nums: &[i32]) -> bool {
    let mut seen: HashSet<i32> = HashSet::new();

    let x = 10;

    for &n in nums {
        return !seen.insert(n) || continue;
    }

    false
}

fn main() {
    let mut nums: &[i32];
    nums =  &[1,3,4,2];
    assert!(!contains_duplicate(&nums));

    nums = &[1,1,1,3,3,4,3,2,4,2];
    assert!(contains_duplicate(&nums));
}
