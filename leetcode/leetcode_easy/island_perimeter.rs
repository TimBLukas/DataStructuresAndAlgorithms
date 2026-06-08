// Optional imports
// use std::collections::HashMap;
// use std::collections::HashSet;

// Leetcode 463: Island Perimeter
// You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water
// Grid cells are connected horizontally/vertically (not diagonally). THe grid is completly sourrounded by water, and there is exactly one island

// The island doesn't have lakes, meaning the water inside isn't connected to the water around the island. Once cell is a square with side length 1.
// The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island

// Examples:
// Input=[[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]; Output = 16
 
pub struct Solution;

impl Solution {
pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
    let mut count = 0;

    for (i, row) in grid.iter().enumerate() {
        for (j, &cell) in row.iter().enumerate() {
            if cell == 1 {
                // oben
                if i == 0 || grid[i - 1][j] != 1 {
                    count += 1;
                }

                // unten
                if i + 1 >= grid.len() || grid[i + 1][j] != 1 {
                    count += 1;
                }

                // links
                if j == 0 || grid[i][j - 1] != 1 {
                    count += 1;
                }

                // rechts
                if j + 1 >= row.len() || grid[i][j + 1] != 1 {
                    count += 1;
                }
            }
        }
    }

    count
}
}