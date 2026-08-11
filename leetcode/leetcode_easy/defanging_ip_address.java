class Main {
  public static void main(String[] args) {
    Solution s = new Solution();
    String defangedAddr = s.defangIPadddr("1.1.1.1");

    IO.println(defangedAddr);
  }
}

class Solution {
  public String defangIPadddr(String address) {
    return address.replace(".", "[.]");
  }
}
