package homework1;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

public class FrontBookkeeper61866 implements IFrontBookkeeper {
	private HashMap<String, LinkedList<Integer>> mapOfSoldiers = new HashMap<String, LinkedList<Integer>>();

	public FrontBookkeeper61866() {
	}

	public String updateFront(String[] news) {
		putSoldiersInMap(news);
		
		for (int i = 0; i < news.length; i++) {
			String[] splitted = news[i].split(" ");
			if (news[i].contains("show")) {

				if (splitted.length == 2) {
					System.out.println(mapOfSoldiers.get(splitted[1]));
				} else if (splitted.length == 3) {
					getKeyFromValue(mapOfSoldiers, splitted[2]);
					System.out.println(getKeyFromValue(mapOfSoldiers,
							splitted[2]));
				}
			}
			if (news[i].contains("attached")) {
				LinkedList<Integer> initialList = mapOfSoldiers
						.get(splitted[3]);
				LinkedList<Integer> secondlList = mapOfSoldiers
						.get(splitted[0]);

				for (int j = 0; j < secondlList.size(); j++) {
					if (news[i].contains("after")) {
						for (int k = 0; k < initialList.size(); k++) {
							if (initialList.get(k) == Integer
									.parseInt(splitted[6])) {
								initialList.add(secondlList.get(j));
							}
						}
						if (mapOfSoldiers.containsValue(initialList)) {
							for (String key : mapOfSoldiers.keySet()) {
								if (!key.equals(splitted[3])) {
									LinkedList<Integer> listOfCommonValues = mapOfSoldiers
											.get(key);
									if (listOfCommonValues.equals(initialList)) {
										listOfCommonValues.clear();

									}

								}
							}

						}
						break;
					}
					initialList.add(secondlList.get(j));
				}
			}
			if (news[i].contains("died")) {
				String deadSoldier = splitted[3];
				String rangeIndexes = splitted[1];
				char firstIndexSplit = rangeIndexes.charAt(0);
				char lastIndexSplit = rangeIndexes.charAt(3);
				LinkedList<Integer> deadListIndexes = new LinkedList<Integer>();
				LinkedList<Integer> listOfSoldier = mapOfSoldiers
						.get(deadSoldier);
				for (int k = 0; k < listOfSoldier.size(); k++) {
					if (listOfSoldier.get(k) == Integer
							.parseInt(firstIndexSplit + "")) {
						while (listOfSoldier.get(k) != Integer
								.parseInt(lastIndexSplit + "")) {
							deadListIndexes.add(listOfSoldier.get(k));
							k += 1;
						}
						deadListIndexes.add(listOfSoldier.get(k));
					}
				}
				for (String value : mapOfSoldiers.keySet()) {
					if (mapOfSoldiers.get(value).containsAll(deadListIndexes)) {
						mapOfSoldiers.get(value).removeAll(deadListIndexes);
					}
				}
			}

		}

		System.out.println(mapOfSoldiers);
		return null;
	}

	public static String getKeyFromValue(
			HashMap<String, LinkedList<Integer>> mapOfSoldiers2, String value) {
		String resultString = "";
		for (String o : mapOfSoldiers2.keySet()) {
			if (mapOfSoldiers2.get(o).contains(Integer.parseInt(value))) {
				resultString += " " + o;
			}
		}
		return resultString;
	}

	public HashMap<String, LinkedList<Integer>> putSoldiersInMap(String[] news) {
		for (int i = 0; i < news.length; i++) {
			if (news[i].contains("=")) {
				String[] soldiersCharacteristics = news[i].split(" = ");
				mapOfSoldiers.put(soldiersCharacteristics[0],
						Soldier.convertToInt(soldiersCharacteristics[1]));
			}
		}
		return mapOfSoldiers;
	}

	public String toString() {
		return "" + mapOfSoldiers;
	}
}
