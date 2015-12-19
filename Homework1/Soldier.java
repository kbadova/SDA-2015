package homework1;

import java.util.LinkedList;

public class Soldier {
	private static LinkedList<Integer> soldiers;

	public static LinkedList<Integer> convertToInt(String str) {
		soldiers = new LinkedList<Integer>();
		for (int i = 0; i < str.length(); i++) {
			if (Character.isDigit(str.charAt(i))) {
				String doubleNumber = str.charAt(i) + "";
				while (Character.isDigit(str.charAt(i + 1))) {
					doubleNumber += str.charAt(i + 1) + "";
					i += 1;
				}
				soldiers.add(Integer.parseInt(doubleNumber));
			}
		}
		return soldiers;
	}

}
