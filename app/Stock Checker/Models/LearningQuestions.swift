//
//  LearningQuestions.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 12.04.21.
//

import Foundation


class LearningQuestions: ObservableObject {
    @Published var level = ""
    
    let quiz = [
        Questions(q: "The investors set the price every time it trades.", a: "True"),//
        Questions(q: "Stocks prices are determined whenever a buyer and seller agree to trade at a given price.", a: "True"),//
        Questions(q: "A broker or a finance website reflects the price as last traded.", a: "True"),//
        Questions(q: "High demand for a stock relative to supply drives the stock price higher.", a: "True"),//
        Questions(q: "A company's dividend is an indicator of how much the stock will grow.", a: "False"),//
        Questions(q: "The demand for a stock goes up through Information(Earnings Report, Press Release, News stories, Court filings, Tweets, General hype, etc.)", a: "True"),//
        Questions(q: "A Company sets the stock price itself.", a: "False"),//
        Questions(q: "A fund is a group of stocks.", a: "True"),//
        Questions(q: "An exchange-traded fund (ETF) that tracks an index, sector, commodity, or other assets. Which can be purchased or sold on a stock exchange the same as a regular stock.", a: "True"),//
        Questions(q: "If you buy a stock today is the price for everyone around the world the same.", a: "False"),
        Questions(q: "The ex-dividend date is the last time when a company will ever pay a dividend again.", a: "False"),
        Questions(q: "Stocks are known as shares in a company. If a company issues 100 shares, and you own 10 shares, then you own 10% of the company.", a: "True")//
    ]
           
}

