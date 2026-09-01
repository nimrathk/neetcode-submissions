// // Definition for a pair
// // class Pair {
// //     int key;
// //     String value;
// //
// //     Pair(int key, String value) {
// //         this.key = key;
// //         this.value = value;
// //     }
// // }
// public class Solution {
//     public List<List<Pair>> insertionSort(List<Pair> pairs) {
//         List<List<Pair>> iterations = new ArrayList<>();
//         List<Pair> thecopy = new ArrayList<>(pairs.size());
//         for (int m = 0; m < pairs.size(); ++m) {
//             thecopy.add(pairs.get(m));
//         }
//         iterations.add(thecopy);

//         for (int i = 1; i < pairs.size(); ++i) {
//             int n = i - 1;
//             while (n > 0 && pairs.get(i).key < pairs.get(n).key) {
//                 n--;
//             }
//             Pair temp = pairs.get(n);
//             pairs.set(n, pairs.get(i));
//             pairs.set(i, temp);
//             List<Pair> copy = new ArrayList<>(pairs.size());
//             for (int z = 0; z < pairs.size(); ++z) {
//                 copy.add(pairs.get(z));
//             }
//             iterations.add(copy);
//         }
//         return iterations;
//     }
// }


public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> iterations = new ArrayList<>();
        
        // Store initial state
        if (pairs.size() != 0) {
            iterations.add(new ArrayList<>(pairs));
        }

        for (int i = 1; i < pairs.size(); ++i) {
            Pair keyPair = pairs.get(i);
            int j = i - 1;

            // Shift elements to the right
            while (j >= 0 && pairs.get(j).key > keyPair.key) {
                pairs.set(j + 1, pairs.get(j));
                j--;
            }

            // Insert keyPair at the correct position
            pairs.set(j + 1, keyPair);

            // Store a snapshot of the current list state
            iterations.add(new ArrayList<>(pairs));
        }
        
        return iterations;
    }

}
