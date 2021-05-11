import { timeConverter } from "./stock"

test("timeConverter", () =>{
    expect(timeConverter(1672444800)).toBe("30 Dec 2022")
    expect(timeConverter(1617148800)).toBe("30 Mar 2021")
})